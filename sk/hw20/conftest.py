import requests
import pytest


@pytest.fixture()
def new_test_post():
    """
    Создает объект для работы с другими тестами и удаляет после завершения
    """
    json = {
        "data": {
            "color": "white",
            "size": "big"
        },
        "name": "Alex"
    }
    response = requests.post("http://167.172.172.115:52353/object", json=json)
    post_id = response.json()["id"]
    yield post_id
    requests.delete(f"http://167.172.172.115:52353/object/{post_id}")


@pytest.fixture(scope="session")
def status_all_test():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture()
def status_test():
    print("before test")
    yield
    print("after test")
