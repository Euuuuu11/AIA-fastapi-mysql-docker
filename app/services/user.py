from app.models.user import User

class UserService(object): 
    def __init__(self) -> None:
        pass
        
        
    def login(self, id, password): 
        users = User(id, password)
        print(f'id : {users.id}')
        print(f'password: {users.password}')
        
        
         