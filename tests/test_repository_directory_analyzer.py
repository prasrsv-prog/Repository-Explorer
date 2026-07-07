from pathlib import Path

from repository_explorer.analysis.repository_directory_analyzer import (
    RepositoryDirectoryAnalyzer,
)
from repository_explorer.model.repository_node import RepositoryNode
from repository_explorer.model.repository_snapshot import RepositorySnapshot


def test_repository_directory_analyzer() -> None:

    snapshot = RepositorySnapshot(
        repository_nodes=[
            RepositoryNode(
                path=Path("src"),
                is_directory=True,
            ),
            RepositoryNode(
                path=Path("src/model"),
                is_directory=True,
            ),
            RepositoryNode(
                path=Path("tests"),
                is_directory=True,
            ),
            RepositoryNode(
                path=Path("README.md"),
                is_directory=False,
            ),
        ]
    )

    analyzer = RepositoryDirectoryAnalyzer()

    result = analyzer.analyze(snapshot)

    assert result.total_directories == 3

    assert result.top_level_directories == [
        "src",
        "tests",
    ]

    assert result.maximum_depth == 2
