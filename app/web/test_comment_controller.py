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


def test_put_existing_comment_should_update_the_comment():
    thread_id = str(uuid.uuid4())
    response = httpx.put(f"http://localhost/threads/{thread_id}", json={'title': 'my_title'})
    thread_id = response.json()['_id']

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
    new_title = 'new_title'
    assert status.HTTP_201_CREATED == response.status_code
    expected_comment = comment_to_insert.copy()
    expected_comment['title'] = new_title
    response = httpx.put(f"http://localhost/comments/{comment_id}",
              json=expected_comment)
    assert status.HTTP_200_OK == response.status_code

    assert_comment_was_updated(expected_comment), "Comment wasn't updated"


def assert_comment_was_updated(expected_comment: dict):
    response = httpx.get("http://localhost/threads/")
    assert status.HTTP_200_OK == response.status_code
    id_comment = expected_comment["_id"]
    for thread in response.json():
        for comment in thread['comments']:
            if (comment['_id']) == id_comment:
                assert expected_comment['title'] == comment['title']
                return
    assert False, "comment not found in thread"
