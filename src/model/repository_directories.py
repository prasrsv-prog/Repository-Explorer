from dataclasses import dataclass


@dataclass(frozen=True)
class RepositoryDirectories:
    """
    Represents directory information of a repository.
    """

    total_directories: int
    top_level_directories: list[str]
    maximum_depth: int