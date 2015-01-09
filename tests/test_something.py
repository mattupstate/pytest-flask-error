
from myapp import User


def test_something(app, user):
    with app.app_context():
        user2 = User.query.filter(User.name == 'matt').one()
        assert user2.name == user.name
