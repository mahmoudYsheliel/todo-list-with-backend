from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    userId:int
    title:str
    description:str
    
class TodoSent(BaseModel):
    title:str
    description:str