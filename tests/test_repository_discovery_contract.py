import pytest

from repository_explorer.contracts.repository_discovery import RepositoryDiscovery


def test_repository_discovery_is_abstract() -> None:
    with pytest.raises(TypeError):
        RepositoryDiscovery()
