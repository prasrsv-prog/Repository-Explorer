from dataclasses import dataclass

from src.model.repository_snapshot import RepositorySnapshot
from src.model.repository_statistics import RepositoryStatistics


@dataclass(frozen=True)
class RepositoryExploration:
    """
    Represents the result of exploring a repository.
    """

    snapshot: RepositorySnapshot
    statistics: RepositoryStatistics