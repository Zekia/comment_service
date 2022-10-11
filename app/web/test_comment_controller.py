import random
import uuid

import httpx
from starlette import status


def test_put_comment_should_create_a_comment():
    # Making sure we have a thread
    thread_id = str(uuid.uuid4())
    response = httpx.put(f"http://localhost/threads/{thread_id}", json={'title': 'my_title'})
    thread_id = response.json()['_id']
    assert thread_id

    comment_id = str(uuid.uuid4())
    comment_to_insert = {
        "_id": comment_id,
        "thread_id": thread_id,
        "title": "test_title",
        "author": "test_author",
        "content": "test_content",
        "image": "test_image"
    }
    response = httpx.put(f"http://localhost/comments/{comment_id}",
                         json=comment_to_insert)

    assert response.status_code == 201
    json_response = response.json()
    assert ['_id', "title", "author", "content", "image"] == list(json_response.keys())
    del comment_to_insert['thread_id']
    assert comment_to_insert == json_response


def test_put_comment_with_unknow_thread_should_return_404():
    thread_id = random.randint(1, 10000)
    comment_id = str(uuid.uuid4())
    comment_to_insert = {
        "_id": comment_id,
        "thread_id": thread_id,
        "title": "test_title",
        "author": "test_author",
        "content": "test_content",
        "image": "test_image"
    }

    response = httpx.put(f"http://localhost/comments/{thread_id}",
                         json=comment_to_insert)
    assert status.HTTP_400_BAD_REQUEST == response.status_code
    expected_body = {
      "detail": f"Thread with ID {thread_id} not found"
    }
    assert expected_body == response.json()