from fastapi import FastAPI
from hello.router import router as router_hello

app = FastAPI(title='hello')

app.include_router(router_hello)