from pathlib import Path

from src.discovery.filesystem_repository_discovery import (
    FilesystemRepositoryDiscovery,
)


def test_discover_repository() -> None:

    discovery = FilesystemRepositoryDiscovery()

    snapshot = discovery.discover(Path("."))

    assert len(snapshot.repository_nodes) > 0