from src.cache.db import UserService
from random import choice


def test_user_service():
    size: int = 100
    ids = [id for id in range(size)]
    us = UserService(dbSize=size,maxCacheSize=10)
    u = us.get_user_by_id(choice(ids))
    print(u)
    assert u is not None


if __name__ == "__main__":
    test_user_service()