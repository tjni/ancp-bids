import gzip
import os
import struct
import tempfile

import pytest

from ancpbids import validate_dataset, DatasetOptions
from ancpbids.schema.headers import (
    _decompress_gzip_prefix,
    _read_nifti_bytes,
    parse_gzip,
    parse_nifti_header,
    axis_codes,
)
from ancpbids.vfs import LocalVfs
from ancpbids.schema.validate import _value_matches, _load_binary_headers
from ..base_test_case import DS005_DIR
from tests.load_helpers import load_test_dataset


def _write_minimal_nifti_gz(path):
    raw = bytearray(348)
    struct.pack_into('<i', raw, 0, 348)
    struct.pack_into('<8h', raw, 40, 3, 4, 4, 4, 1, 1, 1, 1)
    struct.pack_into('<8f', raw, 76, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0)
    struct.pack_into('<B', raw, 123, 10)
    struct.pack_into('<h', raw, 252, 1)
    struct.pack_into('<h', raw, 254, 1)
    struct.pack_into('<4f', raw, 280, 1, 0, 0, 0)
    struct.pack_into('<4f', raw, 296, 0, 1, 0, 0)
    struct.pack_into('<4f', raw, 312, 0, 0, 1, 0)
    raw[344:348] = b'n+1\x00'
    with gzip.open(path, 'wb') as handle:
        handle.write(raw)


def test_parse_gzip_minimal():
    path = _temp_path('.gz')
    with open(path, 'wb') as handle:
        handle.write(b'\x1f\x8b\x08\x00\x01\x00\x00\x00\x00\x03')
    try:
        result = parse_gzip(path)
        assert result is not None
        assert result['timestamp'] == 1
    finally:
        os.unlink(path)


def _temp_path(suffix: str) -> str:
    handle = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
    path = handle.name
    handle.close()
    return path


def test_parse_nifti_header_synthetic():
    path = _temp_path('.nii.gz')
    try:
        _write_minimal_nifti_gz(path)
        header = parse_nifti_header(path)
        assert header is not None
        assert header['shape'] == [4, 4, 4]
        assert header['axis_codes'] == ['R', 'A', 'S']
        gzip_meta = parse_gzip(path)
        assert gzip_meta is not None
    finally:
        os.unlink(path)


def test_decompress_gzip_prefix_matches_full_decompress():
    path = _temp_path('.nii.gz')
    try:
        _write_minimal_nifti_gz(path)
        with open(path, 'rb') as handle:
            compressed = handle.read()
        with gzip.open(path, 'rb') as handle:
            full = handle.read()
        partial = _decompress_gzip_prefix(compressed, 540)
        assert partial == full[:540]
    finally:
        os.unlink(path)


def test_read_nifti_bytes_streams_local_file():
    path = _temp_path('.nii.gz')
    try:
        _write_minimal_nifti_gz(path)
        with gzip.open(path, 'rb') as handle:
            full = handle.read()
        header_bytes = _read_nifti_bytes(path, LocalVfs())
        assert header_bytes == full[:540]
    finally:
        os.unlink(path)


def test_local_vfs_read_bytes_range():
    path = _temp_path('.bin')
    try:
        payload = b'abcdefgh'
        with open(path, 'wb') as handle:
            handle.write(payload)
        vfs = LocalVfs()
        assert vfs.read_bytes_range(path, 2, 3) == b'cde'
        assert vfs.read_bytes_range(path, 0, 0) == b''
    finally:
        os.unlink(path)


def test_axis_codes_identity():
    affine = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]
    assert axis_codes(affine) == ['R', 'A', 'S']


def test_value_matches_constraints():
    assert _value_matches(3, {'type': 'integer', 'minimum': 1, 'maximum': 5})
    assert not _value_matches(0, {'type': 'integer', 'minimum': 1})
    assert _value_matches('abc', {'type': 'string', 'pattern': '[a-z]+'})
    assert not _value_matches('A', {'type': 'string', 'pattern': '[a-z]+'})
    assert _value_matches(
        [1, 2],
        {'type': 'array', 'minItems': 2, 'maxItems': 2, 'items': {'type': 'integer'}})


def test_load_binary_headers_into_context():
    path = _temp_path('_bold.nii.gz')
    try:
        _write_minimal_nifti_gz(path)

        class _File:
            name = os.path.basename(path)
            extension = '.nii.gz'

            def get_absolute_path(self):
                return path

        ctx = {}
        _load_binary_headers(_File(), ctx)
        assert ctx['nifti_header']['shape'] == [4, 4, 4]
        assert ctx['gzip'] is not None
    finally:
        os.unlink(path)


@pytest.mark.parametrize('lazy_loading', [True, False])
def test_validation_subject_context(lazy_loading, paths_mode):
    dataset = load_test_dataset(DS005_DIR, DatasetOptions(lazy_loading=lazy_loading), paths_mode=paths_mode)
    report = validate_dataset(dataset)
    session = report._schema_session
    events = None
    for file in session.iter_files():
        if getattr(file, 'suffix', None) == 'events':
            events = file
            break
    assert events is not None
    ctx = session.context(events, rich=True)
    assert ctx['subject'] is not None
    assert 'ses_dirs' in ctx['subject']['sessions']
    assert report.has_errors()
