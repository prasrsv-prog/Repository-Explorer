from repository_explorer.discovery.filesystem_repository_discovery import FilesystemRepositoryDiscovery
from repository_explorer.explorer.repository_explorer import RepositoryExplorer
from repository_explorer.model.repository_exploration import RepositoryExploration
from repository_explorer.model.repository_node import RepositoryNode


def create_repository_explorer() -> RepositoryExplorer:
    return RepositoryExplorer(
        FilesystemRepositoryDiscovery()
    )


__all__ = [
    "create_repository_explorer",
    "RepositoryExplorer",
    "RepositoryExploration",
    "RepositoryNode",
]
