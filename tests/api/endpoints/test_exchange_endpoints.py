from fastapi.testclient import TestClient
from requests import Response
from starlette import status

from tests.utils.constants import EXCHANGES_ENDPOINT


def test_get_exchanges(client: TestClient):
    url: str = EXCHANGES_ENDPOINT
    response: Response = client.get(url=url)
    assert status.HTTP_200_OK == response.status_code
