import tempfile

import ancpbids.model_base
from ancpbids import load_dataset
from ..base_test_case import *


class PicklingTestCase(BaseTestCase):

    def test_pickling(self):
        ds005: ancpbids.model_base.Dataset = load_dataset(DS005_DIR)
        ents_orig = ds005.query_entities()
        ds_pickled_dir = tempfile.mkdtemp()
        ancpbids.pickle_dataset(ds005, ds_pickled_dir)
        ds_unpickled = ancpbids.unpickle_dataset(ds_pickled_dir)
        self.assertIsNotNone(ds_unpickled)
        ents_unpickled = ds005.query_entities()
        self.assertEqual(ents_orig, ents_unpickled)

        # TODO add more exhaustive assertions to make sure the unpickled dataset behaves as expected
        # alternatively, introduce parameterized tests to existing unit tests
        # by providing a freshly loaded dataset and an unpickled dataset


if __name__ == '__main__':
    unittest.main()
