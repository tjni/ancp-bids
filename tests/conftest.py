import pytest


@pytest.fixture(params=[False, True], ids=['scan', 'paths'])
def paths_mode(request):
    """Whether dataset loads use directory scan (False) or a path manifest (True)."""
    return request.param
