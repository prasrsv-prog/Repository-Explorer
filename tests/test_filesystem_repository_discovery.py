from pathlib import Path

from repository_explorer.discovery.filesystem_repository_discovery import (
    FilesystemRepositoryDiscovery,
)


def test_discover_repository() -> None:

    discovery = FilesystemRepositoryDiscovery()

    snapshot = discovery.discover(Path("."))

    assert len(snapshot.repository_nodes) > 0
