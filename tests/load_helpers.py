"""Test helpers for loading datasets in scan vs path-manifest mode."""
from __future__ import annotations

import os
from typing import Optional, Sequence

from ancpbids import DatasetOptions, load_dataset
from ancpbids.vfs import Vfs


def collect_dataset_paths(root: str) -> list[str]:
    """Collect relative file paths from a dataset directory."""
    paths: list[str] = []
    for dirpath, _, filenames in os.walk(root):
        rel_dir = os.path.relpath(dirpath, root)
        if rel_dir == '.':
            rel_dir = ''
        for filename in filenames:
            rel_path = os.path.join(rel_dir, filename) if rel_dir else filename
            paths.append(rel_path.replace('\\', '/'))
    return sorted(paths)


def load_test_dataset(
        base_dir: str,
        options: Optional[DatasetOptions] = None,
        *,
        paths_mode: bool = False,
        vfs: Optional[Vfs] = None,
        paths: Optional[Sequence[str]] = None):
    """Load a dataset for tests, optionally from a pre-collected path manifest."""
    kwargs = {}
    if vfs is not None:
        kwargs['vfs'] = vfs
    if paths is not None:
        kwargs['paths'] = list(paths)
    elif paths_mode:
        kwargs['paths'] = collect_dataset_paths(str(base_dir))
    return load_dataset(str(base_dir), options, **kwargs)


def load_test_layout(
        base_dir: str,
        options: Optional[DatasetOptions] = None,
        *,
        paths_mode: bool = False,
        vfs: Optional[Vfs] = None):
    from ancpbids.pybids_compat import BIDSLayout

    kwargs = {}
    if vfs is not None:
        kwargs['vfs'] = vfs
    if paths_mode:
        kwargs['paths'] = collect_dataset_paths(str(base_dir))
    return BIDSLayout(str(base_dir), options=options, **kwargs)
