from src.model.repository_directories import RepositoryDirectories
from src.model.repository_snapshot import RepositorySnapshot


class RepositoryDirectoryAnalyzer:
    """
    Calculates directory information from a repository snapshot.
    """

    def analyze(
        self,
        snapshot: RepositorySnapshot,
    ) -> RepositoryDirectories:

        directories = [
            node
            for node in snapshot.repository_nodes
            if node.is_directory
        ]

        top_level_directories = sorted(
            [
                node.path.name
                for node in directories
                if len(node.path.parts) == 1
            ]
        )

        maximum_depth = 0

        for node in directories:
            depth = len(node.path.parts)

            if depth > maximum_depth:
                maximum_depth = depth

        return RepositoryDirectories(
            total_directories=len(directories),
            top_level_directories=top_level_directories,
            maximum_depth=maximum_depth,
        )