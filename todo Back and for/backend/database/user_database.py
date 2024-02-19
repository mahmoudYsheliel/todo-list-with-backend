from models.user import UserInDB,User
from models.runtime import ServiceResponse
from database.mongo_driver import get_database
from lib.crypto import verify_password


async def create_user(user: UserInDB) -> ServiceResponse:
    mdb_result = await get_database().get_collection("user").insert_one(user.model_dump())
    user_id = str(mdb_result.inserted_id)
    return ServiceResponse(data={"user_id": user_id})


async def validate_user(username: str, password: str) -> ServiceResponse:
    # check user in database
    user = await get_database().get_collection("user").find_one({"username": username})
    
    if not user:
        return False

    # check password hash
    user = UserInDB.model_validate(user)
    
    if not verify_password(password, user.hash_password):
        return False
    return True
   

