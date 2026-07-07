from dataclasses import dataclass

from repository_explorer.model.repository_snapshot import RepositorySnapshot
from repository_explorer.model.repository_statistics import RepositoryStatistics
from repository_explorer.model.repository_extensions import RepositoryExtensions
from repository_explorer.model.repository_directories import RepositoryDirectories


@dataclass(frozen=True)
class RepositoryExploration:
    """
    Complete structural information about a repository.
    """

    snapshot: RepositorySnapshot

    statistics: RepositoryStatistics

    extensions: RepositoryExtensions

    directories: RepositoryDirectories
