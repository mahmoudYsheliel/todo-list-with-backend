from pydantic import BaseModel

class User(BaseModel):
    username:str
    password:str
    
class UserInDB(BaseModel):
    id: int
    username:str
    hash_password:str