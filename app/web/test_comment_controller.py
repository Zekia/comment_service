import httpx


def test_put_comment_should_create_a_comment():
    # Making sure we have a thread
    response = httpx.put("http://localhost/threads/", json={'title': 'my_title'})
    print(response.json())
    thread_id = response.json()['_id']
    assert thread_id

    comment_to_insert = {
        "thread_id": thread_id,
        "title": "test_title",
        "author": "test_author",
        "content": "test_content",
        "image": "test_image"
    }
    response = httpx.put("http://localhost/comments/",
                         json=comment_to_insert)

    assert response.status_code == 201
    json_response = response.json()
    assert ['_id', "title", "author", "content", "image"] == list(json_response.keys())
    del json_response['_id']
    del comment_to_insert['thread_id']
    assert comment_to_insert == json_response
