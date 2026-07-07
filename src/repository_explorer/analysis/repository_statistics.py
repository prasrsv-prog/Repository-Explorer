from repository_explorer.model.repository_snapshot import RepositorySnapshot
from repository_explorer.model.repository_statistics import RepositoryStatistics


class RepositoryStatisticsAnalyzer:
    """
    Calculates basic statistics from a repository snapshot.
    """

    def analyze(
        self,
        snapshot: RepositorySnapshot,
    ) -> RepositoryStatistics:

        total_nodes = snapshot.count()

        total_files = sum(
            1
            for node in snapshot.repository_nodes
            if not node.is_directory
        )

        total_directories = sum(
            1
            for node in snapshot.repository_nodes
            if node.is_directory
        )

        return RepositoryStatistics(
            total_nodes=total_nodes,
            total_files=total_files,
            total_directories=total_directories,
        )
