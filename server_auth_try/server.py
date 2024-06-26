from fastapi import FastAPI
from routes11 import auth_router

server = FastAPI()

server.include_router(auth_router.router)

@server.get('/')
def test_hi():
    print("got request to test")
    return "hi from server"

