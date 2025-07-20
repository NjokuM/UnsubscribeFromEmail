from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from routes.gmail_routes import router as gmail_router

app = FastAPI()

origins = ["http://localhost:3000", "http://localhost:3001", "http://localhost", "https://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def get_messages():
    return {"message": "Hello from /"}

app.include_router(gmail_router, prefix="/api")  # or prefix="" if you want it at root
