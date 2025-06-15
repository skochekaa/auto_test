import requests
import allure
from endpoints.endpoint import Endpoint


class PutPost(Endpoint):
    @allure.step("Обновление объекта")
    def update_post(self, post_id):
        self.data = {
            "data": {
                "color": "white",
                "size": "big"
            },
            "id": post_id,
            "name": "New name"
        }
        self.response = requests.put(f"{self.url}/{post_id}", json=self.data)
        self.json = self.response.json()
        return self.response
