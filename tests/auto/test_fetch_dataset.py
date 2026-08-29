
import os.path
import tempfile
from ancpbids import utils
from tests.load_helpers import load_test_dataset

def test_fetch_dataset(paths_mode):
    with tempfile.TemporaryDirectory() as temp_dir:
        ds_path = utils.fetch_dataset('ds003483', output_dir=temp_dir)
        assert os.path.join(temp_dir, 'ds003483') == ds_path
        dataset = load_test_dataset(ds_path, paths_mode=paths_mode)

        # some basic checks to make sure the dataset is downloaded and unzipped as expected
        assert dataset.name == 'ds003483'

        entities = dataset.query_entities()
        assert len(entities["subject"]) == 21
        suffixes = dataset.query(target="suffixes")
        assert suffixes == ['channels', 'coordsystem', 'events', 'meg', 'scans']
