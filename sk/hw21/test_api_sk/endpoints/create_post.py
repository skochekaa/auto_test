import requests
import allure
from endpoints.endpoint import Endpoint


class CreatePost(Endpoint):
    post_id = 0

    @allure.step("Создание нового поста")
    def create_new_post(self, data):
        self.response = requests.post(self.url, json=data)
        self.post_id = self.response.json()["id"]
        self.json = self.response.json()
        return self.response
