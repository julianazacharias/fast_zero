from http import HTTPStatus

from fastapi.testclient import TestClient
from sqlalchemy import select

from fast_zero.app import app
from fast_zero.models import User


def test_root_deve_retornar_ok_e_ola_mundo(client):
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_create_user(session):
    new_user = User(username='alice', password='secret', email='teste@test')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert user.username == 'alice'


# def test_read_users(client):
#     response = client.get('/users/')
#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {
#         'users': [
#             {
#                 'username': 'alice',
#                 'email': 'alice@example.com',
#                 'id': 1,
#             }
#         ]
#     }


# def test_update_user(client):
#     response = client.put(
#         '/users/1',
#         json={
#             'username': 'bob',
#             'email': 'bob@example.com',
#             'password': 'mynewpassword',
#         },
#     )
#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {
#         'username': 'bob',
#         'email': 'bob@example.com',
#         'id': 1,
#     }


# def test_delete_user(client):
#     response = client.delete('/users/1')

#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {'message': 'User deleted'}
