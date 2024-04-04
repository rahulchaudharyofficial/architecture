from cache.db import UserDb

def test_user_db():
    udb = UserDb(5)
    print(udb)
    assert udb is not None