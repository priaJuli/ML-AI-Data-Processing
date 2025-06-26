# routers/items.py
from typing import Annotated, List
from fastapi import APIRouter, Depends

import auth
import schemas

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

@router.get("/")
async def read_items(
    current_user: Annotated[dict, Depends(auth.get_current_user)]
):
    """
    A protected endpoint that returns a list of items.
    Only accessible to authenticated users.
    """
    return [
        {"item_id": "Foo", "owner": current_user["username"]},
        {"item_id": "Bar", "owner": current_user["username"]}
    ]
