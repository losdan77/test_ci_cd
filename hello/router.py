from fastapi import APIRouter

router = APIRouter(
    prefix='/hello',
    tags=['Основа']
)

@router.get('/hello')
async def hello_world():
    return 'hello wrld'
