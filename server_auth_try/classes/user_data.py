from pydantic import BaseModel

class user_Data(BaseModel):
    username: str
    password: str