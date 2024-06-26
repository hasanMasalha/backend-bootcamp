from pydantic import BaseModel
from typing import List

class PokemonSchema(BaseModel):
    name: str
    height: float
    weight: float
    types: List[str]
