"""Virtual filesystem abstraction for dataset I/O."""
from __future__ import annotations

import os
import posixpath
from typing import Optional, Protocol, Sequence, runtime_checkable

_DEFAULT_VFS: Optional["LocalVfs"] = None


@runtime_checkable
class Vfs(Protocol):
    def is_dir(self, path: str) -> bool: ...

    def is_file(self, path: str) -> bool: ...

    def exists(self, path: str) -> bool: ...

    def listdir(self, path: str) -> Sequence[str]: ...

    def read_text(self, path: str, encoding: str = "utf-8") -> str: ...

    def read_bytes(self, path: str) -> bytes: ...

    def write_text(self, path: str, content: str, encoding: str = "utf-8") -> None: ...

    def write_bytes(self, path: str, content: bytes) -> None: ...

    def getsize(self, path: str) -> int: ...

    def makedirs(self, path: str) -> None: ...


class LocalVfs:
    """POSIX filesystem backend (default)."""

    @staticmethod
    def _local_path(path: str) -> str:
        return os.path.normpath(path.replace("\\", "/"))

    def is_dir(self, path: str) -> bool:
        return os.path.isdir(self._local_path(path))

    def is_file(self, path: str) -> bool:
        return os.path.isfile(self._local_path(path))

    def exists(self, path: str) -> bool:
        return os.path.exists(self._local_path(path))

    def listdir(self, path: str) -> Sequence[str]:
        return os.listdir(self._local_path(path))

    def read_text(self, path: str, encoding: str = "utf-8") -> str:
        with open(self._local_path(path), encoding=encoding) as handle:
            return handle.read()

    def read_bytes(self, path: str) -> bytes:
        with open(self._local_path(path), "rb") as handle:
            return handle.read()

    def write_text(self, path: str, content: str, encoding: str = "utf-8") -> None:
        with open(self._local_path(path), "w", encoding=encoding) as handle:
            handle.write(content)

    def write_bytes(self, path: str, content: bytes) -> None:
        with open(self._local_path(path), "wb") as handle:
            handle.write(content)

    def getsize(self, path: str) -> int:
        return os.path.getsize(self._local_path(path))

    def makedirs(self, path: str) -> None:
        local_path = self._local_path(path)
        if not os.path.exists(local_path):
            os.makedirs(local_path)


def default_vfs() -> LocalVfs:
    global _DEFAULT_VFS
    if _DEFAULT_VFS is None:
        _DEFAULT_VFS = LocalVfs()
    return _DEFAULT_VFS


def resolve_vfs(vfs: Optional[Vfs] = None) -> Vfs:
    return vfs if vfs is not None else default_vfs()


def dataset_vfs(model) -> Vfs:
    from ancpbids.model_base import Dataset

    current = model
    while current is not None:
        if isinstance(current, Dataset):
            stored = getattr(current, "_vfs", None)
            if stored is not None:
                return stored
            break
        current = getattr(current, "parent_object_", None)
    return default_vfs()


def call_with_supported_kwargs(func, /, *args, **kwargs):
    """Invoke *func* passing only keyword arguments it accepts."""
    import inspect

    params = inspect.signature(func).parameters
    supported = {
        key: value
        for key, value in kwargs.items()
        if key in params and value is not None
    }
    return func(*args, **supported)


def split_rel_path(rel_path: str) -> list[str]:
    normalized = rel_path.replace("\\", "/")
    return [part for part in normalized.split("/") if part]


def join_path(*parts: str) -> str:
    return posixpath.normpath(posixpath.join(*parts))
