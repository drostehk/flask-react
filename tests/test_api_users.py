# -*- coding: utf-8 -*-
"""
    test_api_users
    ~~~~~~~~~~~~~~

    API users tests
"""


from utils import authenticate, json_of_response, logout


def test_get_users(client):
    default_users = {'users':
                     [
                         {'admin': True,
                          'email': 'admin@tuto.app',
                          'key': 1,
                          'username': 'admin'},
                         {'admin': False,
                          'email': 'user@tuto.app',
                          'key': 2,
                          'username': 'user'}
                     ]}
    authenticate(client)
    response = client.get(
        '/api/user/list/',
    )
    logout
    assert response.status_code == 200
    assert json_of_response(response) == default_users
