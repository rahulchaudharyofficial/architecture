from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str = ''
    age: int = 0


class UserServiceException (Exception):
     pass


class UserService:
    def __init__(self, dbSize: int, maxCacheSize: int) -> None:
          # Initialize database
          self.__db : UserDb = UserDb(dbSize=dbSize)
          self.__cache: UserCache = UserCache()
          self.__MAX_CACHE_SIZE: int = maxCacheSize
          self.cache_size = 0

    def get_user_by_id(self,id: int) -> User:
         user = self.__cache[id]
         if user is None: # cache miss
              user = self.__db[id]
              if user is None: # db miss
                   raise UserServiceException(f'User does not exist with id = {id}')
              else:
                   #if len(self.__cache) < self.__MAX_CACHE_SIZE:
                   self.__cache[id] = user # add to cache for next hit
                   self.cache_size = self.cache_size + 1
                   #else:
                   #    print('No plan for it for now')
                   return user # db hit
         else:
            return user # cache hit



class UserCache:
     def __init__(self) -> None:
          self.__cache : list[User] = []
     
     def __len__(self):
          return len(self.__cache)
     
     def __getitem__(self, id) -> User:
          if id < len(self.__cache):
            return self.__cache[id]
          else:
              return None
     
     def __setitem__(self, id: int, user: User) -> None:
          self.__cache.insert(id,user)

     def get_cache_user_by_id(self, id) -> User:
         if id < len(self.__cache):
            return self.__cache[id]
         else:
              return None


class UserDb:
    def __init__(self, dbSize: int) -> None:
        self.__users : list[User] = [User(id = i, name= f'User-{i}', age=(i+1)) for i in range(dbSize)]

    def __getitem__(self, key):
         return self.__users[key]
    
    def __repr__(self) -> str:
         return f'{self.__users}'
    
    def __str__(self) -> str:
         return f'{self.__users}'
    
    def get_user_by_id(self, id):
         return self.__users[id]