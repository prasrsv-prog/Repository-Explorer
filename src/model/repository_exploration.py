from dataclasses import dataclass

from src.model.repository_snapshot import RepositorySnapshot
from src.model.repository_statistics import RepositoryStatistics
from src.model.repository_extensions import RepositoryExtensions
from src.model.repository_directories import RepositoryDirectories


@dataclass(frozen=True)
class RepositoryExploration:
    """
    Complete structural information about a repository.
    """

    snapshot: RepositorySnapshot

    statistics: RepositoryStatistics

    extensions: RepositoryExtensions

    directories: RepositoryDirectories