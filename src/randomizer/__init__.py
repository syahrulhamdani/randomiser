import requests
from requests.exceptions import RequestException

from randomizer.config import RESOURCE_TO_ENDPOINT
from randomizer.exception import ResourceNotFound, RandomizerReadError


class Randomizer:
    """A random generator class of anything.

    For detailed resources see here:
    https://random-data-api.com/documentation
    """
    def __init__(self, resource="food", size=5, is_xml=True):
        self.resource = resource
        if resource not in RESOURCE_TO_ENDPOINT.keys():
            raise ResourceNotFound(
                f"Resource {self.resource} not found. "
                f"Available resources:\n{self._list_resources()}"
            )
        self.size = size
        self.is_xml = is_xml

    @property
    def endpoint(self):
        if not hasattr(self, "_endpoint"):
            endpoint = RESOURCE_TO_ENDPOINT.get(self.resource)
            setattr(self, "_endpoint", endpoint)
        return getattr(self, "_endpoint")

    def _list_resources(self):
        available_resource = ", ".join(list(RESOURCE_TO_ENDPOINT.keys()))
        return available_resource

    def get(self):
        """Get resources.

        Returns:
            dict: A dictionary representing resources.
        """
        uri = "https://random-data-api.com/api" + self.endpoint
        payload = {
            "size": self.size,
            "is_xml": self.is_xml
        }
        try:
            res = requests.get(uri, params=payload)
            res.raise_for_status()
        except RequestException as err:
            raise RandomizerReadError("Failed to get resources.\n{}".format(err))

        return res.json()
