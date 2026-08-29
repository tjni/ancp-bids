from ancpbids import DatasetOptions, load_dataset, validate_dataset
from ancpbids.vfs import LocalVfs

from ..base_test_case import DS005_DIR
from ..load_helpers import collect_dataset_paths


class RecordingVfs(LocalVfs):
    def __init__(self):
        super().__init__()
        self.read_paths = []

    def read_text(self, path, encoding="utf-8"):
        self.read_paths.append(path)
        return super().read_text(path, encoding)


def test_lazy_contents_use_dataset_vfs():
    vfs = RecordingVfs()
    paths = collect_dataset_paths(DS005_DIR)
    dataset = load_dataset(
        DS005_DIR,
        DatasetOptions(lazy_loading=True, ignore_pickle_file=True),
        vfs=vfs,
        paths=paths,
    )
    assert vfs.read_paths  # schema / eager steps during load

    read_count = len(vfs.read_paths)
    contents = dataset.participants_tsv.contents
    assert contents is not None
    assert len(contents) == 16
    assert len(vfs.read_paths) > read_count


def test_validate_with_lazy_loading_uses_dataset_vfs():
    vfs = RecordingVfs()
    paths = collect_dataset_paths(DS005_DIR)
    dataset = load_dataset(
        DS005_DIR,
        DatasetOptions(lazy_loading=True, ignore_pickle_file=True),
        vfs=vfs,
        paths=paths,
    )
    vfs.read_paths.clear()

    report = validate_dataset(dataset)
    assert report is not None
    assert vfs.read_paths
