from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.routers import auth, users, todos
from fast_zero.schemas import Message

app = FastAPI(title='TheBestGeneratorUserApi')

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todos.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}
