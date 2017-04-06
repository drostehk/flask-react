from app.database import db
from flask_security.utils import hash_password


def init_db(user_datastore):
    db.create_all()
    role_admin = user_datastore.create_role(
        name='admin',
        description="administration user"
    )
    role_user = user_datastore.create_role(
        name='user',
        description="general user"
    )
    admin = user_datastore.create_user(
        email='admin@tuto.app',
        username='admin',
        active=True,
        password=hash_password('password')
    )
    user = user_datastore.create_user(
        email='user@tuto.app',
        username='user',
        active=True,
        password=hash_password('password')
    )
    user_datastore.add_role_to_user(admin, role_user)
    user_datastore.add_role_to_user(user, role_user)
    user_datastore.add_role_to_user(admin, role_admin)

    db.session.commit()


__all__ = ['user']
