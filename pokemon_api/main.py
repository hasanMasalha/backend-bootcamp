from fastapi import FastAPI
from pokemonsRouter import pokemon_router
from trainersRouter import trainer_router
from image_services import imageRouter   

app = FastAPI()

app.include_router(pokemon_router)
app.include_router(trainer_router)
#the image should have a server not a router
####app.include_router(imageRouter.image_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the pokemon API"}
