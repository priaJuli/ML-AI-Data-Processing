# routers/posts.py
from typing import Annotated, List
from fastapi import APIRouter, Depends

import auth
import schemas
from database import fake_posts_db

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)

@router.post("/", response_model=schemas.Post)
async def create_post(
    post: schemas.PostCreate,
    current_user: Annotated[dict, Depends(auth.get_current_user)]
):
    """
    Creates a new post for the authenticated user.
    """
    new_post_id = len(fake_posts_db) + 1
    new_post = {
        "id": new_post_id,
        "title": post.title,
        "content": post.content,
        "owner_username": current_user["username"]
    }
    fake_posts_db.append(new_post)
    return new_post


@router.get("/", response_model=List[schemas.Post])
async def read_posts():
    """
    Returns a list of all posts. This is a public endpoint.
    """
    return fake_posts_db
