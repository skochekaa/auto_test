import requests

url_api = "http://167.172.172.115:52353/object"


def new_test_post(url: str) -> int:
    """
    Создает объект для работы с другими тестами
    :param url:
    :return: id созданного объекта
    """
    json = {
        "data": {
            "color": "white",
            "size": "big"
        },
        "name": "Alex"
    }
    response = requests.post(url, json=json)
    return response.json()["id"]


def clear(url: str, id_obj: int):
    """
    Чистит данные после запроса
    :param url:
    :param id_obj:
    :return:
    """
    requests.delete(f"{url}/{id_obj}")


def get_all_objects(url: str):
    """
    Получает список всех объектов
    :param url: url/endpoint
    :return:
    """
    response = requests.get(url)
    print(response.json())


def get_one_objects(url: str, id_obj: int):
    """
     Получает один объект по заданному id
    :param url: url/endpoint
    :param id_obj: id нужного объекта
    :return: assert полученного id с принятым
    """
    response = requests.get(f"{url}/{id_obj}")
    assert response.json()["id"] == id_obj, "Получен объект с другим id"


def post_new_object(url: str):
    """
    Добавляет новый объект
    :param url:
    :return: assert добавленное объекта по имени
    """
    json = {
        "data": {
            "color": "black",
            "size": "M"
        },
        "name": "Alex Sk"
    }
    response = requests.post(url, json=json)
    assert response.json()["name"] == "Alex Sk", "Объект не создан"
    assert response.status_code == 200, "Status code incorrect"
    clear(url, response.json()["id"])


def put_object(url: str, id_obj: int):
    """
    Изменение объекта методом PUT
    :param url:
    :param id_obj:
    :return: assert измененного объекта по имени
    """
    json = {
        "data": {
            "color": "white",
            "size": "big"
        },
        "id": id_obj,
        "name": "New name"
    }
    response = requests.put(f"{url}/{id_obj}", json=json)
    assert response.json()["name"] == "New name", "PUT запрос не выполнен"
    clear(url, id_obj)


def patch_post(url: str, id_obj: int):
    """
    Изменение объекта методом PATCH
    :param url:
    :param id_obj:
    :return:
    """
    json = {
        "data": {
            "color": "black",
        },
    }
    response = requests.patch(f"{url}/{id_obj}", json=json)
    assert response.json()["data"]["color"] == "black", "PATCH запрос не выполнен"
    clear(url, id_obj)


def delete_object(url: str, id_obj: int):
    """
    Удаляет объект по принятому id
    :param url:
    :param id_obj:
    :return:
    """
    response = requests.delete(f"{url}/{id_obj}")
    assert response.status_code == 200, "Не удалось удалить объект"


get_all_objects(url_api)
get_one_objects(url_api, new_test_post(url_api))
post_new_object(url_api)
put_object(url_api, new_test_post(url_api))
patch_post(url_api, new_test_post(url_api))
delete_object(url_api, new_test_post(url_api))
