import httpx

def test_put_thread():
    response = httpx.put("http://localhost/threads/", json={'id': 'test', 'title': 'my_title', 'comments': 'my_comments'})
    # Assert HTTP code and if received document id is valid
    assert response.status_code == 201
    assert list(response.json().keys()) == ['_id', 'title', 'comments']

def test_read_thread():
    response = httpx.get("http://localhost/threads/")
    # Assert HTTP code and if received document id is valid
    assert response.status_code == 200
    assert list(response.json()[0].keys()) == ['_id', 'title', 'comments']

