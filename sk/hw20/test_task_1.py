import requests
import pytest
import allure


@allure.feature("GET-запрос")
def test_get_all_objects(status_all_test, status_test):
    """
    Получает список всех объектов
    """
    response = requests.get("http://167.172.172.115:52353/object")
    assert len(response.json()) > 0, "Посты не получены"


@allure.feature("GET-запрос")
def test_get_one_objects(status_test, new_test_post):
    """
     Получает один объект по заданному id
    """
    response = requests.get(f"http://167.172.172.115:52353/object/{new_test_post}")
    assert response.json()["id"] == new_test_post, "Получен объект с другим id"


@allure.feature("POST-запрос")
@pytest.mark.parametrize("name", ["Angela", "Lex", "Bob"])
def test_post_new_object(status_test, name):
    """
    Добавляет новый объект
    """
    json = {
        "data": {
            "color": "black",
            "size": "M"
        },
        "name": name
    }
    response = requests.post("http://167.172.172.115:52353/object", json=json)
    print(response.json()["name"])
    assert response.json()["name"] == name, "Объект не создан"
    assert response.status_code == 200, "Status code incorrect"


@allure.feature("PUT-запрос")
@pytest.mark.critical()
def test_put_object(status_test, new_test_post):
    """
    Изменение объекта методом PUT
    """
    json = {
        "data": {
            "color": "white",
            "size": "big"
        },
        "id": new_test_post,
        "name": "New name"
    }
    response = requests.put(f"http://167.172.172.115:52353/object/{new_test_post}", json=json)
    assert response.json()["name"] == "New name", "PUT запрос не выполнен"


@allure.feature("PATCH-запрос")
@pytest.mark.medium()
def test_patch_post(status_test, new_test_post):
    """
    Изменение объекта методом PATCH
    """
    json = {
        "data": {
            "color": "black",
        },
    }
    response = requests.patch(f"http://167.172.172.115:52353/object/{new_test_post}", json=json)
    assert response.json()["data"]["color"] == "black", "PATCH запрос не выполнен"


@allure.feature("DELETE-запрос")
def test_delete_object(status_test, new_test_post):
    """
    Удаляет объект по принятому id
    """
    response = requests.delete(f"http://167.172.172.115:52353/object/{new_test_post}")
    assert response.status_code == 200, "Не удалось удалить объект"
