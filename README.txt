$ py.test -s tests
========================================== test session starts ===============================================
platform darwin -- Python 2.7.6 -- py-1.4.26 -- pytest-2.6.4
collected 1 items

tests/test_something.py ('on_teardown', (AttributeError("'Function' object has no attribute 'callspec'",),), {})
('on_teardown', (NoResultFound('No row was found for one()',),), {})
F

======== FAILURES ========
___________________________________________ test_something ___________________________________________________

app = <Flask 'myapp'>, user = <myapp.User object at 0x109942ad0>

    def test_something(app, user):
        with app.app_context():
>           user2 = User.query.filter(User.name == 'matt').one()

tests/test_something.py:7:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <flask_sqlalchemy.BaseQuery object at 0x109946d10>

    def one(self):
        """Return exactly one result or raise an exception.

            Raises ``sqlalchemy.orm.exc.NoResultFound`` if the query selects
            no rows.  Raises ``sqlalchemy.orm.exc.MultipleResultsFound``
            if multiple object identities are returned, or if multiple
            rows are returned for a query that does not return object
            identities.

            Note that an entity query, that is, one which selects one or
            more mapped classes as opposed to individual column attributes,
            may ultimately represent many rows but only one row of
            unique entity or entities - this is a successful result for one().

            Calling ``one()`` results in an execution of the underlying query.

            .. versionchanged:: 0.6
                ``one()`` fully fetches all results instead of applying
                any kind of limit, so that the "unique"-ing of entities does not
                conceal multiple object identities.

            """
        ret = list(self)

        l = len(ret)
        if l == 1:
            return ret[0]
        elif l == 0:
>           raise orm_exc.NoResultFound("No row was found for one()")
E           NoResultFound: No row was found for one()

../../../.virtualenvs/blahblah/lib/python2.7/site-packages/sqlalchemy/orm/query.py:2401: NoResultFound
