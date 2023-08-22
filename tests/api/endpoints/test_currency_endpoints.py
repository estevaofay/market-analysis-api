from fastapi.testclient import TestClient
from requests import Response
from starlette import status

from tests.utils.constants import CURRENCIES_ENDPOINT


def test_get_currencies(client: TestClient):
    url: str = CURRENCIES_ENDPOINT
    response: Response = client.get(url=url)
    assert status.HTTP_200_OK == response.status_code
