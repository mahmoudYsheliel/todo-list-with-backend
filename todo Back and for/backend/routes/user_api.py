from fastapi import APIRouter, Body,Depends,status
from lib.crypto import create_access_token,get_password_hash
from models.runtime import ServiceResponse
from database.mongo_driver import get_database
from typing import Annotated
from fastapi.security import  OAuth2PasswordRequestForm
from database.user_database import validate_user,create_user
from datetime import  timedelta
from models.token import Token
from models.user import User,UserInDB


router = APIRouter()

async def get_userid(username):
    id=await get_database().get_collection('user').find_one({'username':username},{'id':1,'_id':0})
    return  id['id']

@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token|ServiceResponse:
    valid = await validate_user(form_data.username,form_data.password)
    if not valid:
        return ServiceResponse(success=False,msg="no such user")

    userid = await get_userid(form_data.username)
    access_token_expires = timedelta(minutes=1000)
    access_token = create_access_token(
        data={'userId':userid}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token)

@router.post('/login')
async def login(user:User =Body(embed=True)):
    newid=await get_database().get_collection('user').count_documents({})
    hash_password=get_password_hash(user.password)
    new_user=UserInDB(id=newid,username=user.username,hash_password=hash_password)
    try:
        return await create_user(new_user)
    except:
        return ServiceResponse(success=False,msg="couldn't add user")






