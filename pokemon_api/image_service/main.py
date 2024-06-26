from fastapi import FastAPI
import imageRouter

app = FastAPI()

app.include_router(imageRouter.image_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Image Service"}
