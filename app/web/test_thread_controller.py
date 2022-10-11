import httpx

def test_put_thread_should_create_a_thread():
    response = httpx.put("http://localhost/threads/", json={'title': 'my_title'})
    # Assert HTTP code and if received document id is valid
    assert response.status_code == 201
    json_response = response.json()
    assert list(json_response.keys()) == ['_id', 'title', 'comments']
    del json_response['_id']
    assert json_response == {'title': 'my_title', 'comments': []}

def test_put_thread_should_be_idempotent():
    httpx.put("http://localhost/threads/", json={'id': 'test', 'title': 'my_title', 'comments': 'my_comments'})
    response = httpx.put("http://localhost/threads/", json={'id': 'test', 'title': 'my_title', 'comments': 'my_comments'})
    # Assert HTTP code and if received document id is valid
    assert response.status_code == 201
    assert list(response.json().keys()) == ['_id', 'title', 'comments']

def test_get_threads_should_return_a_list_of_threads():
    response = httpx.get("http://localhost/threads/")
    # Assert HTTP code and if received document id is valid
    assert response.status_code == 200
    assert list(response.json()[0].keys()) == ['_id', 'title', 'comments']

def test_get_one_thread_should_return_thread():
    expected_title = 'my_title'
    response = httpx.put("http://localhost/threads/", json={'title': expected_title})
    thread_id = response.json()['_id']

    response = httpx.get(f"http://localhost/threads/{thread_id}")

    # Assert HTTP code and if received document id is valid
    assert response.status_code == 200
    assert ['_id', 'title', 'comments'] == list(response.json().keys())
    assert expected_title == response.json()['title']
