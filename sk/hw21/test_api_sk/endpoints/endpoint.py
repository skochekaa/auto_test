import allure
import requests


class Endpoint:
    url = "http://167.172.172.115:52353/object"
    response = None
    json = None

    @allure.step("Проверка имени пользователя")
    def check_response_title(self, name):
        assert self.response.json()["name"] == name, "Имя не совпадает"

    @allure.step("Проверка ID пользователя")
    def check_response_id(self, new_post):
        assert self.response.json()["id"] == new_post, "Получен объект с другим id"

    @allure.step("Проверка статус кода == 200")
    def check_status_code_is_200(self):
        assert self.response.status_code == 200, "Статс код некорректный"

    @allure.step("Удаление тестовых данных")
    def delete_self_object(self):
        requests.delete(f"{self.url}/{self.response.json()['id']}")
