import requests
import allure
from endpoints.endpoint import Endpoint


class DeletePost(Endpoint):

    @allure.step("Обновление объекта")
    def delete_post(self, post_id):
        self.response = requests.delete(f"{self.url}/{post_id}")
        return self.response
