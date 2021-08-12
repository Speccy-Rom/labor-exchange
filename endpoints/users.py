from typing import List

from fastapi import APIRouter, Depends
from repositories.users import UserRepository
from models.user import User
from endpoints.depends import get_user_repository


router = APIRouter()


@router.get('/', response_model=List[User])
async def read_users(
        users: UserRepository = Depends(get_user_repository),
        limit: int = 100,
        skip: int = 100):
    return await users.get_all(limit=limit, skip=skip)
