import pytest
import allure

TEST_DATA = [
    {"data": {"color": "black", "size": "M"}, "name": "Alex"},
    {"data": {"color": "white", "size": "S"}, "name": "Bob"},
    {"data": {"color": "red", "size": "X"}, "name": "Max"}
]


@allure.feature("GET-запросы")
@allure.title("Получение всех объектов")
def test_get_all_objects(get_all_post):
    get_all_post.get_all_objects()


@allure.feature("GET-запросы")
@allure.title("Получение одного объекта")
def test_get_one_objects(get_one_post, post_id):
    get_one_post.get_one_objects(post_id=post_id)
    get_one_post.delete_self_object()


@allure.feature("POST-запросы")
@allure.title("Создание нового объекта")
@pytest.mark.parametrize("data", TEST_DATA)
def test_post_new_object(create_post_endpoint, data):
    create_post_endpoint.create_new_post(data=data)
    create_post_endpoint.check_response_title(data["name"])
    create_post_endpoint.delete_self_object()


@allure.feature("PUT-запросы")
@allure.title("Изменение объекта методом PUT")
def test_put_object(put_object, post_id):
    put_object.update_post(post_id=post_id)
    put_object.check_response_title(put_object.data["name"])
    put_object.delete_self_object()


@allure.feature("PATCH-запросы")
@allure.title("Изменение объекта методом PATCH")
def test_patch_object(patch_object, post_id):
    patch_object.update_post(post_id=post_id)
    patch_object.check_response_title(patch_object.data["name"])
    patch_object.delete_self_object()


@allure.feature("DELETE-запросы")
@allure.title("Удаление объекта")
def test_delete_object(delete_object, post_id):
    delete_object.delete_post(post_id)
    delete_object.check_status_code_is_200()
