from fastapi import APIRouter

router = APIRouter(
    prefix='/hello',
    tags=['Основа']
)

@router.post('/hello')
async def hello_world():
    return 'hello wrld'
