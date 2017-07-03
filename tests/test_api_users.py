# -*- coding: utf-8 -*-
"""
    test_users
    ~~~~~~~~~~~~~~

    Users managment tests
"""

from utils import authenticate, logout


# 14-15, 21-27, 33-45, 51-62, 68-74, 80-93, 99-105
def test_get_users(client):
    without_login = client.get('/api/user/list/')
    authenticate(client)
    response = client.get('/api/user/list/')
    logout(client)
    assert without_login.status_code == 302
    assert response.status_code == 200
    assert isinstance(response.json['users'], list)


def test_get_user(client):
    user = {
        "admin": True,
        "email": "admin@tuto.app",
        "key": 1,
        "username": "admin"
    }

    without_login = client.get('/api/user/get/')
    authenticate(client)
    response = client.get('/api/user/get/')
    logout(client)
    assert without_login.status_code == 302
    assert response.status_code == 200
    assert response.json == user


def test_add_user(client):
    data = {
        "username": "testUser",
        "email": "test@tuto.app",
        "password": "testPassword"
    }
    without_login = client.post('/api/user/add/', data=data)
    authenticate(client)
    wrong_method = client.get('/api/user/add/?username=a&email=a@b.c')
    save = client.post('/api/user/add/', data=data)
    mistake = client.post('/api/user/add/',
                          data={"username": "testUserA",
                                "password": "password"})
    logout(client)
    assert without_login.status_code == 302
    assert wrong_method.status_code == 405
    assert {'message': 'saved'} == save.json
    assert {'message': 'failed'} == mistake.json


def test_change_user(client):
    username = 'new_name'
    wrong_method = client.get('/api/user/modify/?username=a&email=a@b.c')
    without_login = client.post('/api/user/modify/')
    authenticate(client)
    user_login = client.get('/api/user/get/').json
    user_login['username'] = username
    user_login['password'] = 'password'
    client.post('/api/user/modify/', data=user_login)
    user_login['password'] = 'fakePassword'
    wrong_password = client.post('/api/user/modify/',
                                 data=user_login).json
    user_login.pop('password')
    form_not_valid = client.post('/api/user/modify/',
                                 data=user_login).json
    user_login = client.get('/api/user/get/').json
    logout(client)
    assert without_login.status_code == 302
    assert wrong_method.status_code == 405
    assert user_login['username'] == username
    assert wrong_password['messageText'] == 'Wrong password'
    assert form_not_valid['messageText'] == 'Failed to save changes'


def test_change_password(client):
    client.post('/api/user/password')


def test_change_admin(client):
    wrong_method = client.get('/api/user/change_admin/?key=2')
    without_login = client.post('/api/user/change_admin/')
    authenticate(client)
    users = client.get('/api/user/list/').json
    user_id = None
    for each in users['users']:
        if not each['admin']:
            user_id = each['key']
            break
    to_admin = client.post('/api/user/change_admin/',
                           data={'key': user_id})
    to_user = client.post('/api/user/change_admin/',
                          data={'key': user_id})
    mistake = client.post('/api/user/change_admin/', data={'key': 0})
    invalid = client.post('/api/user/change_admin/', data={'akey': 0})
    logout(client)
    assert without_login.status_code == 302
    assert wrong_method.status_code == 405
    assert invalid.status_code == 200
    assert {'message': 'saved'} == to_admin.json
    assert {'message': 'saved'} == to_user.json
    assert {'message': 'user not found'} == mistake.json
    assert {'message': 'failed'} == invalid.json


def test_delete_user(client):
    wrong_method = client.get('/api/user/delete/?key=2')
    without_login = client.post('/api/user/delete/')
    authenticate(client)
    users = client.get('/api/user/list/').json
    user_id = None
    for each in users['users']:
        if not each['admin']:
            user_id = each['key']
            break

    delete = client.post('/api/user/delete/', data={'key': user_id})
    invalid = client.post('/api/user/delete/', data={'keyx': user_id})
    mistake = client.post('/api/user/delete/', data={'key': 0})
    logout(client)
    assert without_login.status_code == 302
    assert wrong_method.status_code == 405
    assert delete.status_code == 200
    assert mistake.status_code == 200
    assert invalid.status_code == 200
    assert {'message': 'deleted'} == delete.json
    assert {'message': 'user not found'} == mistake.json
    assert {'message': 'failed'} == invalid.json
