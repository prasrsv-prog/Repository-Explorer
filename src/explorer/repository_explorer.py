from pathlib import Path

from src.analysis.repository_directory_analyzer import (
    RepositoryDirectoryAnalyzer,
)
from src.analysis.repository_extension_analyzer import (
    RepositoryExtensionAnalyzer,
)
from src.analysis.repository_statistics import (
    RepositoryStatisticsAnalyzer,
)
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
        self._extension_analyzer = RepositoryExtensionAnalyzer()
        self._directory_analyzer = RepositoryDirectoryAnalyzer()

    def explore(
        self,
        repository_path: Path,
    ) -> RepositoryExploration:

        snapshot = self._discovery.discover(repository_path)

        statistics = self._statistics_analyzer.analyze(snapshot)
        extensions = self._extension_analyzer.analyze(snapshot)
        directories = self._directory_analyzer.analyze(snapshot)

        return RepositoryExploration(
            snapshot=snapshot,
            statistics=statistics,
            extensions=extensions,
            directories=directories,
        )