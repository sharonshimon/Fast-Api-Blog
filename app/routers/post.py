from fastapi import APIRouter, HTTPException, Response, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from models.post import Post
from db.connection import get_session
from services import post_service

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.get("/")
async def get_posts(session: AsyncSession = Depends(get_session)):
    posts = await post_service.get_posts(session)
    return {"data": posts}

@router.post("/")
async def create_post(post: Post, session: AsyncSession = Depends(get_session)):
    new_post = await post_service.create_post(session, post)
    return {"message": "Post created successfully", "post": new_post}

@router.get("/{id}")
async def get_post(id: int, session: AsyncSession = Depends(get_session)):
    post = await post_service.get_post(session, id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"data": post}

@router.delete("/{id}")
async def delete_post(id: int, session: AsyncSession = Depends(get_session)):
    deleted = await post_service.delete_post(session, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully", "post": deleted}

@router.put("/{id}")
async def update_post(id: int, post: Post, session: AsyncSession = Depends(get_session)):
    updated = await post_service.update_post(session, id, post)
    if not updated:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"data": updated}