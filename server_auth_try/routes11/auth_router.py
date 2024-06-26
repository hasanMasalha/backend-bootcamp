from fastapi import APIRouter
from classes import user_data as c
from utils import auth_fns as fns
from utils import db_fns
router = APIRouter()


@router.post('/auth/sign_up')
def sign_up(body: c.user_Data):
    
    hashed_pass= fns.hash_password(body.password)
    db_fns.save_user_data_db(body.username,hashed_pass)
    print("hi from sign up")
    return "hi from sign up"


