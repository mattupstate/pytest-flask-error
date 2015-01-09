
from flask import ctx

from myapp import app as _app, db, User

import pytest


@pytest.yield_fixture(scope='session')
def app():
    db.create_all(app=_app)
    yield _app
    db.drop_all(app=_app)


@pytest.fixture()
def user(app):
    @app.teardown_appcontext
    def on_teardown(*args, **kwargs):
        print('on_teardown', args, kwargs)

    with app.app_context():
        user = User(name='matt', email='matt@matt.com', password='password')
        db.session.add(user)

    return user
