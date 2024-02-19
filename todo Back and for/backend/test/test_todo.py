import requests
import json
import _test_config

url = _test_config.get_api_url()
token = _test_config.get_token()

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",  # adjust content type as needed
}


# check success create todo
def test_create_todo():
    res = requests.post(
        url + "/create_todo",
        json={"new_todo": {"title": "testpy", "description": "pytest"}},
        headers=headers,
    )
    # check status code
    assert res.status_code == 200
    data = json.loads(res.content)
    # check if response contains id
    assert data["data"]["todo_id"]


# check fail create todo no auth
def test_create_todo_no_auth():
    res = requests.post(
        url + "/create_todo",
        json={"new_todo": {"title": "testpy", "description": "pytest"}},
    )
    # check status code
    assert res.status_code == 401


def test_no_title():
    res = requests.post(
        url + "/create_todo",
        json={"new_todo": {"description": "testpy"}},
        headers=headers,
    )
    assert res.status_code == 422


def test_no_description():
    res = requests.post(
        url + "/create_todo", json={"new_todo": {"title": "testpy"}}, headers=headers
    )
    assert res.status_code == 422


def test_get_todo():
    res = requests.post(url + "/get_todos", headers=headers)
    assert res.status_code == 200
    # check if data is there and contain todos
    todos = res.json()["data"]["todos"]
    assert todos
    # check properities
    assert isinstance(todos, list)
    assert todos[0]["id"]
    assert todos[0]["title"]
    assert todos[0]["description"]


# check unauthorized
def test_get_todo_no_auth():
    res = requests.post(
        url + "/get_todos",
    )
    assert res.status_code == 401


def test_update_todo():
    res = requests.post(
        url + "/update_todo",
        json={'id':0, "new_todo": {"title": "testupdate", "description": "testupdae"}},
        headers=headers
    )
    assert res.status_code == 200
    assert res.json()['data']=={}
    
def test_update_todo_no_title():
    res = requests.post(
        url + "/update_todo",
        json={'id':0, "new_todo": {"description": "testupdae"}},
        headers=headers
    )
    assert res.status_code == 422
    

def test_update_todo_no_description():
    res = requests.post(
        url + "/update_todo",
        json={'id':0, "new_todo": {"title": "testupdate"}},
        headers=headers
    )
    assert res.status_code == 422

def test_update_todo_no_todo():
    res = requests.post(
        url + "/update_todo",
        json={'id':0, },
        headers=headers
    )
    assert res.status_code == 422

def test_update_todo_no_id():
    res = requests.post(
        url + "/update_todo",
        json={'new_todo':{'title':'new','description':'new'} },
        headers=headers
    )
    assert res.status_code == 422





def test_delete_todo():
    res = requests.post(
        url + "/create_todo",
        json={"new_todo": {"title": "testpy", "description": "pytest"}},
        headers=headers,
    )
    data = json.loads(res.content)
    # Extract the todo_id
    todo_id = data["data"]["todo_id"]
    res = requests.post(
        url + "/delete_todo",
        json={"id": todo_id},
        headers=headers,
    )
    assert res.status_code == 200
    assert res.json()['data']=={}

def test_delete_todo_no_aut():
    res = requests.post(
        url + "/create_todo",
        json={"new_todo": {"title": "testpy", "description": "pytest"}},
        headers=headers,
    )
    data = json.loads(res.content)
    # Extract the todo_id
    todo_id = data["data"]["todo_id"]
    res = requests.post(
        url + "/delete_todo",
        json={"id": todo_id},
    )
    assert res.status_code == 401
    
def test_delete_todo_no_id():
    res = requests.post(
        url + "/create_todo",
        json={"new_todo": {"title": "testpy", "description": "pytest"}},
        headers=headers,
    )
    data = json.loads(res.content)
    # Extract the todo_id
    todo_id = data["data"]["todo_id"]
    res = requests.post(
        url + "/delete_todo",
        headers=headers
    )
    assert res.status_code == 422