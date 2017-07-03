# -*- coding: utf-8 -*-
"""
    test_users
    ~~~~~~~~~~~~~~

    Users managment tests
"""


def test_get_users(client):
    client.get('/api/user/get_users')


def test_get_user(client):
    client.get('/api/user/get')


def test_add_user(client):
    client.post('/api/user/add/')


def test_change_user(client):
    client.post('/api/user/modify')


def test_change_password(client):
    client.post('/api/user/password')


def test_change_admin(client):
    client.post('/api/user/admin')


def test_delete_user(client):
    client.post('/api/user/delete/')
