from http import HTTPStatus


def test_read_root_deve_retornar_ola_mundo(client):
    response = client.get('/')

    assert response.json() == {'message': 'Olá Mundo!'}


def test_read_root_deve_retornar_statuscode_200(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
