from pydantic import BaseModel, Field,EmailStr

class postSchema(BaseModel):
    id: int = Field(default=None)
    name: str = Field (default= None)
    classes: list = Field(default=None)
    role : str = Field(default=None)
    class config: 
        schema_extra = {
            "post_demo": {
                "name":"user name",
                "classes":"user classes",
                "role": "user role"

            }
        }
class userSchema(BaseModel):
    fullname: str = Field(default = None)
    email: EmailStr = Field(default=  None)
    password : str = Field(default= None)
    class config:
        the_schema = {
            "user_demo": {
                "name" :"name",
                "email" : "example@example.com",
                "password": "123" 
            }
        }

class userLoginSchema(BaseModel):
    email: EmailStr = Field(default=  None)
    password : str = Field(default= None)
    class config:
        the_schema = {
            "user_demo": {
                "email" : "example@example.com",
                "password": "123" 
            }
        }
