import pytest
from endpoints.create_post import CreatePost
from endpoints.get_all_objects import GetAllObjects
from endpoints.get_one_object import GetOneObjects
from endpoints.put_post import PutPost
from endpoints.patch_post import PatchPost
from endpoints.delete_post import DeletePost


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def get_all_post():
    return GetAllObjects()


@pytest.fixture()
def get_one_post():
    return GetOneObjects()


@pytest.fixture()
def post_id(create_post_endpoint):
    data = {"data": {"color": "black", "size": "M"}, "name": "Test User"}
    create_post_endpoint.create_new_post(data)
    return create_post_endpoint.post_id


@pytest.fixture()
def put_object():
    return PutPost()


@pytest.fixture()
def patch_object():
    return PatchPost()


@pytest.fixture()
def delete_object():
    return DeletePost()
