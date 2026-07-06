from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RepositoryNode:
    """
    Represents a single node inside a repository.
    """

    path: Path
    is_directory: bool