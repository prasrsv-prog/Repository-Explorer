from pathlib import Path

from src.model.repository_node import RepositoryNode


def test_create_repository_node() -> None:

    node = RepositoryNode(
        path=Path("images/logo.png"),
        is_directory=False,
    )

    assert node.path == Path("images/logo.png")
    assert node.is_directory is False