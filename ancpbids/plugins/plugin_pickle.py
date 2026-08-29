import pickle
import posixpath
from types import ModuleType

from ancpbids import utils
from ancpbids.model_base import Dataset
from ancpbids.vfs import dataset_vfs, resolve_vfs

ANCP_BIDS_SCHEMA_VERSION = "AncpBIDSSchemaVersion"

ANCPBIDS_PICKLE_FILE = ".ancpbids-dataset.pickle"


class DatasetPickler(pickle.Pickler):

    def persistent_id(self, obj):
        from ancpbids.schema import Schema
        if isinstance(obj, Schema):
            return (ANCP_BIDS_SCHEMA_VERSION, obj.VERSION)
        if isinstance(obj, ModuleType) and obj.__name__.startswith("ancpbids."):
            return (ANCP_BIDS_SCHEMA_VERSION, obj.VERSION)
        return None


class DatasetUnpickler(pickle.Unpickler):

    def persistent_load(self, pid):
        type_tag, key_id = pid
        if type_tag == "AncpBIDSSchemaVersion":
            return utils.get_schema_by_version(key_id)

        raise pickle.UnpicklingError(f"unsupported persistent object: {pid}")


def pickle_dataset(dataset, custom_dir=None):
    resolved_vfs = dataset_vfs(dataset)
    ds_path = posixpath.join(custom_dir or dataset.get_absolute_path(), ANCPBIDS_PICKLE_FILE)
    resolved_vfs.write_bytes(ds_path, _dump_dataset(dataset))


def unpickle_dataset(dataset_path, vfs=None) -> Dataset:
    resolved_vfs = resolve_vfs(vfs)
    ds_path = posixpath.join(dataset_path, ANCPBIDS_PICKLE_FILE)
    ds = _load_dataset(resolved_vfs.read_bytes(ds_path))
    ds._vfs = resolved_vfs
    return ds


def _dump_dataset(dataset) -> bytes:
    import io
    buffer = io.BytesIO()
    DatasetPickler(buffer).dump(dataset)
    return buffer.getvalue()


def _load_dataset(payload: bytes) -> Dataset:
    import io
    return DatasetUnpickler(io.BytesIO(payload)).load()
