from pathlib import Path

from src.analysis.repository_statistics import RepositoryStatisticsAnalyzer
from src.contracts.repository_discovery import RepositoryDiscovery
from src.model.repository_exploration import RepositoryExploration


class RepositoryExplorer:
    """
    Coordinates repository exploration.
    """

    def __init__(
        self,
        discovery: RepositoryDiscovery,
    ) -> None:
        self._discovery = discovery
        self._statistics_analyzer = RepositoryStatisticsAnalyzer()

    def explore(
        self,
        repository_path: Path,
    ) -> RepositoryExploration:

        snapshot = self._discovery.discover(repository_path)

        statistics = self._statistics_analyzer.analyze(snapshot)

        return RepositoryExploration(
            snapshot=snapshot,
            statistics=statistics,
        )