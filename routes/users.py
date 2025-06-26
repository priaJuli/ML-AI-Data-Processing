# routers/users.py
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

import auth
import schemas
from database import fake_users_db

router = APIRouter(
    prefix="/users",  # All routes in this router will start with /users
    tags=["users"]    # Tag for API docs
)

@router.post("/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate):
    """
    Creates a new user.
    """
    if user.username in fake_users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    hashed_password = auth.get_password_hash(user.password)
    fake_users_db[user.username] = {"username": user.username, "hashed_password": hashed_password}
    return {"username": user.username}


@router.get("/me/", response_model=schemas.User)
async def read_users_me(
    current_user: Annotated[dict, Depends(auth.get_current_user)]
):
    """
    Fetches the details of the currently authenticated user.
    """
    # In a real app, you might fetch more user details from the DB here
    return current_user
