from pathlib import Path

from src.model.repository_node import RepositoryNode
from src.model.repository_snapshot import RepositorySnapshot


def test_create_repository_snapshot() -> None:

    node = RepositoryNode(
        path=Path("README.md"),
        is_directory=False,
    )

    snapshot = RepositorySnapshot(
        repository_nodes=[node],
    )

    assert len(snapshot.repository_nodes) == 1