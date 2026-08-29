
from ancpbids import DatasetOptions
from tests.base_test_case import DS005_DIR_IGNORED_RESOURCES
from tests.load_helpers import load_test_dataset

import pytest

@pytest.mark.parametrize("lazy_loading", [True, False])
def test_ignore_file(lazy_loading, paths_mode):
    ds = load_test_dataset(
        DS005_DIR_IGNORED_RESOURCES,
        DatasetOptions(ignore=True, lazy_loading=lazy_loading),
        paths_mode=paths_mode,
    )
    assert ds.get_folder("models") is None
    assert ds.get_folder("stimuli") is None
    assert ds.get_file(".dummy") is None
    assert ds.query(sub="01", suffix="bold") is not None
    assert ds.dataset_description is not None
    assert ds.get_file(".bidsignore") is None

@pytest.mark.parametrize("lazy_loading", [True, False])
def test_ignore_file_dynamic(lazy_loading, paths_mode):
    ds = load_test_dataset(
        DS005_DIR_IGNORED_RESOURCES,
        DatasetOptions(ignore=["models", "stimuli", ".*"], lazy_loading=lazy_loading),
        paths_mode=paths_mode,
    )
    assert ds.get_folder("models") is None
    assert ds.get_folder("stimuli") is None
    assert ds.get_file(".dummy") is None
    assert ds.query(sub="01", suffix="bold") is not None
    assert ds.dataset_description is not None
    assert ds.get_file(".bidsignore") is None
