from pathlib import Path

from repository_explorer.contracts.repository_discovery import RepositoryDiscovery
from repository_explorer.model.repository_node import RepositoryNode
from repository_explorer.model.repository_snapshot import RepositorySnapshot


class FilesystemRepositoryDiscovery(RepositoryDiscovery):
    """
    Discovers repository structure from the local filesystem.
    """

    def discover(self, repository_path: Path) -> RepositorySnapshot:

        repository_nodes: list[RepositoryNode] = []

        for path in repository_path.rglob("*"):
            repository_nodes.append(
                RepositoryNode(
                    path=path.relative_to(repository_path),
                    is_directory=path.is_dir(),
                )
            )

        return RepositorySnapshot(
            repository_nodes=repository_nodes,
        )
