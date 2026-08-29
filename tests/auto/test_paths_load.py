import pytest

from ancpbids import DatasetOptions
from tests.base_test_case import DS005_DIR, DS005_DIR_IGNORED_RESOURCES, DS005_SMALL_DIR
from tests.load_helpers import collect_dataset_paths, load_test_dataset


def dataset_file_paths(dataset) -> list[str]:
    schema = dataset.get_schema()
    return sorted(
        file.get_relative_path().replace('\\', '/')
        for file in dataset.select(schema.File).objects()
    )


@pytest.mark.parametrize("dataset_dir", [DS005_SMALL_DIR, DS005_DIR])
@pytest.mark.parametrize("lazy_loading", [True, False])
def test_load_dataset_from_paths_matches_directory_scan(dataset_dir, lazy_loading):
    """Explicit regression: path manifest produces the same graph as directory scan."""
    options = DatasetOptions(lazy_loading=lazy_loading, ignore_pickle_file=True)
    manifest = collect_dataset_paths(dataset_dir)

    scanned = load_test_dataset(dataset_dir, options, paths_mode=False)
    from_manifest = load_test_dataset(dataset_dir, options, paths=manifest)

    assert dataset_file_paths(scanned) == dataset_file_paths(from_manifest)


@pytest.mark.parametrize("lazy_loading", [True, False])
def test_load_dataset_from_paths_respects_bidsignore(lazy_loading):
    options = DatasetOptions(ignore=True, lazy_loading=lazy_loading, ignore_pickle_file=True)
    manifest = collect_dataset_paths(DS005_DIR_IGNORED_RESOURCES)

    scanned = load_test_dataset(DS005_DIR_IGNORED_RESOURCES, options, paths_mode=False)
    from_manifest = load_test_dataset(DS005_DIR_IGNORED_RESOURCES, options, paths=manifest)

    for dataset in (scanned, from_manifest):
        assert dataset.get_folder("models") is None
        assert dataset.get_folder("stimuli") is None
        assert dataset.get_file(".dummy") is None
        assert dataset.query(sub="01", suffix="bold") is not None

    assert dataset_file_paths(scanned) == dataset_file_paths(from_manifest)
