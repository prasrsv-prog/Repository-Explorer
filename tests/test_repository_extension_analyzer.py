from pathlib import Path

from repository_explorer.analysis.repository_extension_analyzer import (
    RepositoryExtensionAnalyzer,
)
from repository_explorer.model.repository_node import RepositoryNode
from repository_explorer.model.repository_snapshot import RepositorySnapshot


def test_repository_extension_analyzer() -> None:

    snapshot = RepositorySnapshot(
        repository_nodes=[
            RepositoryNode(
                path=Path("README.md"),
                is_directory=False,
            ),
            RepositoryNode(
                path=Path("main.py"),
                is_directory=False,
            ),
            RepositoryNode(
                path=Path("photo.JPG"),
                is_directory=False,
            ),
            RepositoryNode(
                path=Path("LICENSE"),
                is_directory=False,
            ),
            RepositoryNode(
                path=Path("src"),
                is_directory=True,
            ),
        ]
    )

    analyzer = RepositoryExtensionAnalyzer()

    result = analyzer.analyze(snapshot)

    assert result.extensions[".md"] == 1
    assert result.extensions[".py"] == 1
    assert result.extensions[".jpg"] == 1
    assert result.extensions["<no_extension>"] == 1

    assert ".zip" not in result.extensions
