from repository_explorer.model.repository_extensions import RepositoryExtensions
from repository_explorer.model.repository_snapshot import RepositorySnapshot


class RepositoryExtensionAnalyzer:
    """
    Calculates extension statistics from a repository snapshot.
    """

    def analyze(
        self,
        snapshot: RepositorySnapshot,
    ) -> RepositoryExtensions:

        extensions: dict[str, int] = {}

        for node in snapshot.repository_nodes:

            if node.is_directory:
                continue

            extension = node.path.suffix.lower()

            if not extension:
                extension = "<no_extension>"

            extensions[extension] = (
                extensions.get(extension, 0) + 1
            )

        return RepositoryExtensions(
            extensions=extensions,
        )
