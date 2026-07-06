from dataclasses import dataclass


@dataclass(frozen=True)
class RepositoryStatistics:
    """
    Represents basic repository statistics.
    """

    total_nodes: int
    total_files: int
    total_directories: int