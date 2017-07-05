from app.database import db
from flask import Blueprint, jsonify, request
from flask_security import roles_required, current_user
from flask_security.utils import encrypt_password, verify_password
from app.models.user import Role, get_user, get_username, get_users
from app.forms.user import Add, Change, Select

user_bp = Blueprint('user', __name__)


@user_bp.route('/get/', methods=['GET'])
@roles_required('user')
def user():
    user = get_username(current_user.username)
    return jsonify(user.get_setup())


@user_bp.route('/list/', methods=['GET'])
@roles_required('admin')
def users():
    users = {}
    user = get_username(current_user.username)
    if user.is_admin():
        users.update(get_users())
    else:
        users.update({'users': []})
    return jsonify(users)


@user_bp.route('/add/', methods=['POST'])
@roles_required('admin')
def user_add():
    form = Add(request.form)
    if form.validate():
        user = get_user(0)
        user.username = form.username.data
        current_user.username = user.username
        user.email = form.email.data
        user.password = encrypt_password(form.password.data)
        role_user = Role.query.filter(Role.name == 'user').first()
        user.roles.append(role_user)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'saved'})
    return jsonify({'message': 'failed'})


@user_bp.route('/modify/', methods=['POST'])
@roles_required('user')
def user_change():
    form = Change(request.form)
    if form.validate_on_submit():
        user = get_user(form.key.data)
        if verify_password(form.password.data, user.password):
            user.username = form.username.data
            user.email = form.email.data
            if form.password.data != '':
                user.password = (form.password.data)
            db.session.commit()
            return jsonify({"messageMode": 0, "messageText": "Changes saved "})
        return jsonify({"messageMode": 1, "messageText": "Wrong password"})
    return jsonify({"messageMode": 1, "messageText": "Failed to save changes"})


@user_bp.route('/change_admin/', methods=['POST'])
@roles_required('admin')
def user_change_admin():
    form = Select(request.form)
    if form.validate():
        user = get_user(form.key.data)
        if form.key.data == 0:
            user = None
        try:
            user.change_admin()
            db.session.commit()
            return jsonify({'message': 'saved'})
        except:
            return jsonify({'message': 'user not found'})
    return jsonify({'message': 'failed'})


@user_bp.route('/delete/', methods=['POST'])
@roles_required('admin')
def user_delete():
    form = Select(request.form)
    if form.validate():
        user = get_user(form.key.data)
        if form.key.data == 0:
            user = None
        try:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'deleted'})
        except:
            return jsonify({'message': 'user not found'})
    return jsonify({'message': 'failed'})
