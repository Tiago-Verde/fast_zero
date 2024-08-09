from http import HTTPStatus


def test_create_todo_valida_statuscode(client, token):
    response = client.post(
        '/todos',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'title': 'test todo',
            'description': 'test description',
            'state': 'draft',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'title': 'test todo',
        'description': 'test description',
        'state': 'draft',
        'id': 1
    }
