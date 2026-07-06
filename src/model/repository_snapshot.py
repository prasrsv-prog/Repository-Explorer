from dataclasses import dataclass

from src.model.repository_node import RepositoryNode


@dataclass(frozen=True)
class RepositorySnapshot:
    """
    Represents an immutable snapshot of a repository.
    """

    repository_nodes: list[RepositoryNode]

    def count(self) -> int:
        return len(self.repository_nodes)