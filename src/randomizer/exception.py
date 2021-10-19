"""Exception modules."""


class RandomizerError(Exception):
    """Base class for all exceptions in randomizer."""
    pass


class ResourceNotFound(RandomizerError):
    """Error due to resource is not available."""
    pass


class RandomizerReadError(RandomizerError):
    """Error due to failed get request."""
    pass
