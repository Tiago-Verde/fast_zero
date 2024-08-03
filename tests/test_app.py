from http import HTTPStatus

from fast_zero.schemas import UserPublic


def test_read_root_deve_retornar_ola_mundo(client):
    response = client.get('/')

    assert response.json() == {'message': 'Olá Mundo!'}


def test_read_root_deve_retornar_statuscode_200(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK


def test_create_user_deve_retornar_statuscode_201(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED


def test_create_user_deve_retornar_payload_de_resposta_correto(client):
    response = client.post(
        '/users/',
        json={
            'username': 'mario',
            'email': 'mario@example.com',
            'password': 'secret',
        },
    )

    assert response.json() == {
        'username': 'mario',
        'email': 'mario@example.com',
        'id': 1,
    }


def test_read_user_deve_retornar_statuscode_200(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK


def test_read_user_deve_retornar_lista_de_usuario_vazia(client):
    response = client.get('/users/')

    assert response.json() == {'users': []}


def test_read_user_deve_retornar_payload_de_resposta_correto(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')

    assert response.json() == {'users': [user_schema]}


def test_update_user_deve_retornar_statuscode_200(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == HTTPStatus.OK


def test_update_user_deve_retornar_payload_de_resposta_correta(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'julia',
            'email': 'julia@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.json() == {
        'username': 'julia',
        'email': 'julia@example.com',
        'id': 1,
    }


def test_update_user_valida_statuscode_404_usuario_nao_encontrado(client):
    response = client.put(
        '/users/5',
        json={
            'username': 'julia',
            'email': 'julia@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user_deve_validar_statuscode_200(client, user):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK


def test_delete_user_valida_payload_de_resposta_correta(client, user):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}


def test_delete_user_valida_statuscode_404(client):
    response = client.delete('/users/5')

    assert response.status_code == HTTPStatus.NOT_FOUND
