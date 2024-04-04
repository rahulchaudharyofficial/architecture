from dataclasses import dataclass
from random import choice

@dataclass
class User:
    id: int
    name: str = ''
    age: int = 0

#def __generate_mock_users(count: int) -> list[User]:
#        assert count > 0
#        users : list[User] = []
#        for i in range(count):
#            users.append(User(id= i, name=f'User-{i+1}', age= (i+1)))
#        return users

class UserDb:
    def __init__(self, dbSize: int) -> None:
        self.users : list[User] = [User(id = i, name= f'User-{i}', age=(i+1)) for i in range(dbSize)]

    def __get_item__(self, key):
         return self.users[key]
    
    def __repr__(self) -> str:
         return f'{self.users}'
    
    def __str__(self) -> str:
         return f'{self.users}'
         
         


