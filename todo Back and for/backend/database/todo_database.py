from models.todo import Todo
from models.runtime import ServiceResponse
from database.mongo_driver import  get_database
from bson.objectid import ObjectId



async def create_todo(todo: Todo) -> ServiceResponse:
    mdb_result = await get_database().get_collection('todo').insert_one(todo.model_dump())
    todo_id =await get_database().get_collection('todo').find_one({'_id':ObjectId(str(mdb_result.inserted_id))},{'id':1,'_id':0})
    return ServiceResponse(data={'todo_id': todo_id['id']})


async def delete_todo(todo_id: int) -> ServiceResponse:
    result = await get_database().get_collection('todo').delete_one({'id': todo_id})
    if not result.deleted_count:
        return ServiceResponse(success=False, status_code=404, msg='todo not Found')
    return ServiceResponse(msg='OK')


async def update_todo(todo_id: int, update: dict) -> ServiceResponse:
    result = await get_database().get_collection('todo').update_one(
        {'id': todo_id}, {'$set': update}
    )
    if not result.modified_count:
        return ServiceResponse(success=False, status_code=404, msg='todo not Found')
    return ServiceResponse(msg='OK')



async def get_todos(userId:int)-> ServiceResponse:
    todos = await get_database().get_collection('todo').find({'userId':userId}, {
        '_id': 0,
        'id': 1,
        'title':1,
        'description':1
    }).to_list(length=None)
    return ServiceResponse(data={'todos': todos})

async def get_todo(todoId:int)-> ServiceResponse:
    todo = await get_database().get_collection('todo').find({'Id':todoId}, {
        '_id': 0,
        'userId':0,
        'title':1,
        'description':1
    }).to_list(length=None)
    return ServiceResponse(data={'todo': todo})


