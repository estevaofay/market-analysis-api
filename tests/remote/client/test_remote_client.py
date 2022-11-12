import pytest

from remote.client.remote_client import RemoteClient


def test_cant_create_instance_of_abc():
    with pytest.raises(TypeError):
        RemoteClient()
