from locust import task, HttpUser
import random


class QAUser(HttpUser):
    url = "http://167.172.172.115:52353/object"

    @task
    def get_all_objects(self):
        self.client.get(self.url)

    @task
    def get_one_object(self):
        self.client.get(f"`{self.url}/{random.choice([1, 2, 3])}")
