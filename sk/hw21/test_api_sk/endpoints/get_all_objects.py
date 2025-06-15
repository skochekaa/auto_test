import requests
import allure
from endpoints.endpoint import Endpoint


class GetAllObjects(Endpoint):
    @allure.step("Получение всех объектов")
    def get_all_objects(self):
        self.response = requests.get(self.url)
        return self.response
