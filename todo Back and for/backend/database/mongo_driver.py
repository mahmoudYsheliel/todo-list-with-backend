import motor.motor_asyncio


mdb_client: motor.motor_asyncio.AsyncIOMotorClient | None = None

async def mongodb_connect():
    connection_string = 'mongodb://root:oDJSwjBHFnIhU2KHBp7L2xf65VcNK9gWBll82Mpmuii1ly8KUYqFODTHx5xvkAht@localhost:27017/'
    global mdb_client
    mdb_client = motor.motor_asyncio.AsyncIOMotorClient(connection_string, serverSelectionTimeoutMS=3000)
    
    

def get_database() ->  motor.motor_asyncio.core.AgnosticDatabase | None:
    if mdb_client:
        return mdb_client.TodoList
    return None

