import uuid

import httpx

def test_put_thread_should_create_a_thread():
    thread_id = str(uuid.uuid4())
    response = httpx.put(f"http://localhost/v1/threads/{thread_id}", json={'title': 'my_title'})
    # Assert HTTP code and if received document id is valid
    assert response.status_code == 201
    json_response = response.json()
    assert ['_id', 'title', 'comments'] == list(json_response.keys())
    assert {'_id': thread_id, 'title': 'my_title', 'comments': []} == json_response

def test_put_thread_should_be_idempotent():
    thread_id = str(uuid.uuid4())
    httpx.put(f"http://localhost/v1/threads/{thread_id}", json={'title': 'my_title'})
    response = httpx.put(f"http://localhost/v1/threads/{thread_id}", json={'title': 'my_title'})
    # Assert HTTP code and if received document id is valid
    assert response.status_code == 200
    assert list(response.json().keys()) == ['_id', 'title', 'comments']

def test_get_threads_should_return_a_list_of_threads():
    response = httpx.get("http://localhost/v1/threads/")
    # Assert HTTP code and if received document id is valid
    assert response.status_code == 200
    assert list(response.json()[0].keys()) == ['_id', 'title', 'comments']

def test_get_one_thread_should_return_thread():
    expected_title = 'my_title'
    thread_id = str(uuid.uuid4())
    response = httpx.put(f"http://localhost/v1/threads/{thread_id}", json={'title': expected_title})
    thread_id = response.json()['_id']

    response = httpx.get(f"http://localhost/v1/threads/{thread_id}")

    # Assert HTTP code and if received document id is valid
    assert response.status_code == 200
    assert ['_id', 'title', 'comments'] == list(response.json().keys())
    assert expected_title == response.json()['title']

def test_update_one_thread():
    old_title = 'my_title'
    thread_id = str(uuid.uuid4())
    response = httpx.put(f"http://localhost/v1/threads/{thread_id}", json={'title': old_title})
    thread_id = response.json()['_id']

    new_title = 'new_title'
    responseUpdate = httpx.put(f"http://localhost/v1/threads/{thread_id}", json={'title': new_title})

    assert responseUpdate.status_code == 200
    responseFind = httpx.get(f"http://localhost/v1/threads/{thread_id}")
    assert new_title == responseFind.json()['title']

def test_remove_one_thread():
    thread_id = str(uuid.uuid4())
    response = httpx.put(f"http://localhost/v1/threads/{thread_id}", json={'title': 'title'})
    thread_id = response.json()['_id']

    response = httpx.delete(f"http://localhost/v1/threads/{thread_id}")
    assert response.status_code == 200
    assert response.json()['id'] == thread_id
    find_response = httpx.get(f"http://localhost/v1/threads/{thread_id}")
    assert find_response.status_code == 400