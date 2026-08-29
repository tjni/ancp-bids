from typing import Optional

from ancpbids.plugin import FileHandlerPlugin, hook
from ancpbids.vfs import resolve_vfs


def read_yaml(file_path: str, **kwargs):
    import yaml

    vfs = resolve_vfs(kwargs.get('vfs'))
    try:
        return yaml.load(vfs.read_text(file_path), Loader=yaml.FullLoader)
    except Exception:
        return None


def read_json(file_path: str, **kwargs):
    import json

    vfs = resolve_vfs(kwargs.get('vfs'))
    try:
        return json.loads(vfs.read_text(file_path))
    except Exception:
        return None


def read_plain_text(file_path: str, **kwargs):
    vfs = resolve_vfs(kwargs.get('vfs'))
    text = vfs.read_text(file_path)
    if not text:
        return []
    return text.splitlines(keepends=True)


def read_tsv(file_path: str, return_type: Optional[str] = None, **kwargs):
    import csv
    import io

    vfs = resolve_vfs(kwargs.get('vfs'))
    if return_type == "ndarray":
        import numpy

        return numpy.genfromtxt(
            io.BytesIO(vfs.read_bytes(file_path)), delimiter='\t', dtype=None, names=True
        )
    if return_type == "dataframe":
        import pandas

        return pandas.read_csv(io.BytesIO(vfs.read_bytes(file_path)), delimiter='\t')
    return list(csv.DictReader(io.StringIO(vfs.read_text(file_path)), dialect="excel-tab"))


def write_json(file_path: str, contents: dict, **kwargs):
    import json

    vfs = resolve_vfs(kwargs.get('vfs'))
    vfs.write_text(file_path, json.dumps(contents, indent=2))


def write_tsv(file_path: str, contents, **kwargs):
    import csv
    import io

    vfs = resolve_vfs(kwargs.get('vfs'))
    if isinstance(contents, str):
        payload = contents
        if payload and not payload.endswith('\n'):
            payload += '\n'
        vfs.write_text(file_path, payload)
        return

    if hasattr(contents, 'to_csv') and hasattr(contents, 'columns'):
        buffer = io.StringIO()
        contents.to_csv(buffer, sep='\t', index=False)
        vfs.write_text(file_path, buffer.getvalue())
        return

    if isinstance(contents, list):
        if not contents:
            vfs.write_text(file_path, '')
            return
        if not isinstance(contents[0], dict):
            raise TypeError(
                "write_tsv list contents must be a list of dict rows, "
                f"got list of {type(contents[0]).__name__}"
            )
        fieldnames = list(contents[0].keys())
        buffer = io.StringIO()
        writer = csv.DictWriter(
            buffer,
            fieldnames=fieldnames,
            delimiter='\t',
            lineterminator='\n',
            extrasaction='ignore',
        )
        writer.writeheader()
        writer.writerows(contents)
        vfs.write_text(file_path, buffer.getvalue())
        return

    raise TypeError(
        "write_tsv expects str, list[dict], or pandas DataFrame, "
        f"got {type(contents).__name__}"
    )


def write_txt(file_path: str, contents: dict, **kwargs):
    vfs = resolve_vfs(kwargs.get('vfs'))
    vfs.write_text(file_path, str(contents))


@hook(ranking=0, system=True)
class FilesHandlerPlugin(FileHandlerPlugin):
    def execute(self, file_readers_registry, file_writers_registry):
        file_readers_registry['yaml'] = read_yaml
        file_readers_registry['json'] = read_json
        file_readers_registry['txt'] = read_plain_text
        file_readers_registry['tsv'] = read_tsv

        file_writers_registry['json'] = write_json
        file_writers_registry['tsv'] = write_tsv
        file_writers_registry['txt'] = write_txt
