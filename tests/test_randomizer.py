import pytest
from randomizer import Randomizer
from randomizer.exception import ResourceNotFound


def test_resource_not_found():
    with pytest.raises(ResourceNotFound):
        randomizer = Randomizer("random")
