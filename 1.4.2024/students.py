from pydantic import BaseModel
class student(BaseModel):
    id: int
    name: str
    classes: list
        