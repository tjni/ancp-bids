import os
import tempfile

import ancpbids.model_base
import ancpbids
from ..base_test_case import DS005_DIR
from tests.load_helpers import load_test_dataset


def test_pickling(paths_mode):
    ds005: ancpbids.model_base.Dataset = load_test_dataset(DS005_DIR, paths_mode=paths_mode)
    ents_orig = ds005.query_entities()
    ds_pickled_dir = tempfile.mkdtemp()
    ancpbids.pickle_dataset(ds005, ds_pickled_dir)
    ds_unpickled = ancpbids.unpickle_dataset(ds_pickled_dir)
    assert ds_unpickled is not None
    ents_unpickled = ds005.query_entities()
    assert ents_orig == ents_unpickled

    # TODO add more exhaustive assertions to make sure the unpickled dataset behaves as expected
