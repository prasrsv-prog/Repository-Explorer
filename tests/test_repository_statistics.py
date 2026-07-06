from pathlib import Path

from src.analysis.repository_statistics import RepositoryStatisticsAnalyzer
from src.model.repository_node import RepositoryNode
from src.model.repository_snapshot import RepositorySnapshot


def test_repository_statistics() -> None:

    snapshot = RepositorySnapshot(
        repository_nodes=[
            RepositoryNode(
                path=Path("README.md"),
                is_directory=False,
            ),
            RepositoryNode(
                path=Path("src"),
                is_directory=True,
            ),
        ]
    )

    analyzer = RepositoryStatisticsAnalyzer()

    statistics = analyzer.analyze(snapshot)

    assert statistics.total_nodes == 2
    assert statistics.total_files == 1
    assert statistics.total_directories == 1