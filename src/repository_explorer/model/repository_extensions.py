from dataclasses import dataclass


@dataclass(frozen=True)
class RepositoryExtensions:
    """
    Represents extension statistics of a repository.
    """

    extensions: dict[str, int]
