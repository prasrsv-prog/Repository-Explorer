from pathlib import Path

from repository_explorer.model.repository_directories import RepositoryDirectories
from repository_explorer.model.repository_extensions import RepositoryExtensions
from repository_explorer.model.repository_exploration import RepositoryExploration
from repository_explorer.model.repository_node import RepositoryNode
from repository_explorer.model.repository_snapshot import RepositorySnapshot
from repository_explorer.model.repository_statistics import RepositoryStatistics


def test_create_repository_exploration() -> None:

    node = RepositoryNode(
        path=Path("README.md"),
        is_directory=False,
    )

    snapshot = RepositorySnapshot(
        repository_nodes=[node],
    )

    statistics = RepositoryStatistics(
        total_nodes=1,
        total_files=1,
        total_directories=0,
    )

    extensions = RepositoryExtensions(
        extensions={
            ".md": 1,
        },
    )

    directories = RepositoryDirectories(
        total_directories=0,
        top_level_directories=[],
        maximum_depth=0,
    )

    exploration = RepositoryExploration(
        snapshot=snapshot,
        statistics=statistics,
        extensions=extensions,
        directories=directories,
    )

    assert exploration.snapshot == snapshot
    assert exploration.statistics.total_nodes == 1
    assert exploration.statistics.total_files == 1
    assert exploration.extensions.extensions[".md"] == 1
    assert exploration.directories.total_directories == 0
