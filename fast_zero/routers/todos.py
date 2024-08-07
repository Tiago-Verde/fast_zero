from fastapi import APIRouter
from fast_zero.schemas import TodoPublic, TodoSchema

router = APIRouter(prefix='/todos', tags=['todos'])


@router.post('/', response_model=TodoPublic)
def create_todo(todo: TodoSchema):
    ...