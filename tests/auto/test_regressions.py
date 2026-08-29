
import ancpbids
from ..base_test_case import DS005_DIR

import pytest
from ancpbids import DatasetOptions
from tests.load_helpers import load_test_dataset

@pytest.mark.parametrize("lazy_loading", [True, False])
def test_get_all_files_from_pipeline(lazy_loading, paths_mode):
    dataset = load_test_dataset(DS005_DIR, DatasetOptions(lazy_loading=lazy_loading), paths_mode=paths_mode)
    all_derivative_files = dataset.query(scope='derivatives/affine/matrix', return_type='file')
    assert len(all_derivative_files) == 16

@pytest.mark.parametrize("lazy_loading", [True, False])
def test_report_errors(lazy_loading, paths_mode):
    dataset = load_test_dataset(DS005_DIR, DatasetOptions(lazy_loading=lazy_loading), paths_mode=paths_mode)
    report = ancpbids.validate_dataset(dataset)
    assert report.has_errors()

@pytest.mark.parametrize("lazy_loading", [True, False])
def test_get_entitites_no_scope(lazy_loading, paths_mode):
    dataset = load_test_dataset(DS005_DIR, DatasetOptions(lazy_loading=lazy_loading), paths_mode=paths_mode)
    entities = dataset.query_entities(scope=None)
    assert ['ds', 'type', 'subject', 'task', 'run', 'description'] == list(entities.keys())
