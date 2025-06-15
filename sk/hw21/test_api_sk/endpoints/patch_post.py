import requests
import allure
from endpoints.endpoint import Endpoint


class PatchPost(Endpoint):

    @allure.step("Обновление объекта методом PATCH")
    def update_post(self, post_id):
        self.data = {
            "name": "New name"
        }
        self.response = requests.patch(f"{self.url}/{post_id}", json=self.data)
        self.json = self.response.json()
        return self.response
