import requests
import allure
from endpoints.endpoint import Endpoint


class GetOneObjects(Endpoint):
    @allure.step("Получение одного объекта")
    def get_one_objects(self, post_id):
        self.response = requests.get(f"{self.url}/{post_id}")
        return self.response
