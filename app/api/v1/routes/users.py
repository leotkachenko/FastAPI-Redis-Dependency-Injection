import uuid
from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from pydantic import UUID4
from app.api.dependecies import cache
from app.dtos.users import UserRequestDTO, UserResponseDTO
from app.models.users import User

router = APIRouter()


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(user_id: UUID4, cache=Depends(cache)) -> UserResponseDTO:
    user = await cache.get(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_users(cache=Depends(cache)) -> list[UserResponseDTO]:
    users = await cache.get_all()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return users


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserRequestDTO,
    cache=Depends(cache),
    background_task: BackgroundTasks = BackgroundTasks(),
) -> UUID4:
    user = User(id=uuid.uuid4(), **user.dict())
    background_task.add_task(cache.set, user.id, user.json())
    return user.id


@router.put("/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(
    user_id: UUID4,
    user_request: UserRequestDTO,
    cache=Depends(cache),
    background_task: BackgroundTasks = BackgroundTasks(),
) -> UUID4:
    existing_user = await cache.get(user_id)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    user = User(id=user_id, **user_request.dict())
    background_task.add_task(cache.set, user.id, user.json())
    return user_id


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(
    user_id: UUID4,
    cache=Depends(cache),
    background_task: BackgroundTasks = BackgroundTasks(),
):
    existing_user = await cache.get(user_id)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    background_task.add_task(cache.delete, user_id)
