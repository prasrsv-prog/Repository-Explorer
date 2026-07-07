from pathlib import Path

from repository_explorer.discovery.filesystem_repository_discovery import (
    FilesystemRepositoryDiscovery,
)
from repository_explorer.explorer.repository_explorer import RepositoryExplorer


def test_repository_explorer() -> None:

    explorer = RepositoryExplorer(
        discovery=FilesystemRepositoryDiscovery(),
    )

    exploration = explorer.explore(Path("."))

    assert exploration.statistics.total_nodes > 0
    assert exploration.statistics.total_files > 0
