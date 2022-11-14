from fastapi.testclient import TestClient
from requests import Response
from starlette import status


def test_healthcheck(client: TestClient):
    response: Response = client.get("/health")
    assert status.HTTP_200_OK == response.status_code
