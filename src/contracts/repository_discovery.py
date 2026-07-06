from abc import ABC, abstractmethod
from pathlib import Path

from src.model.repository_snapshot import RepositorySnapshot


class RepositoryDiscovery(ABC):
    """
    Defines how a repository structure is discovered.
    """

    @abstractmethod
    def discover(self, repository_path: Path) -> RepositorySnapshot:
        """
        Discover a repository and return its snapshot.
        """