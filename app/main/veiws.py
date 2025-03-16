from flask import render_template
from . import blue_main
from .. import db
from ..models import Role, User


@blue_main.route('/', methods=['GET', 'POST'])
def index():
    db.drop_all()
    db.create_all()

    admin_role = Role(name='Admin')
    mod_role = Role(name='Moderator')
    user_role = Role(name='User')
    user_john = User(username='john', role=admin_role)
    user_susan = User(username='susan', role=user_role)
    user_david = User(username='david', role=user_role)

    db.session.add_all([admin_role, mod_role, user_role,
                        user_john, user_susan, user_david])
    db.session.commit()

    tables = []
    for i in range(User.query.count()):
        obj = User.query.get(i + 1)
        tables.append(
            (i + 1, obj.role.name, obj.username, obj.role_id)
        )

    return render_template('index.html',
                           column_role='角色名',
                           column_user='用户名',
                           tables=tables)
