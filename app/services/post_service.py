from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from models.post import Post

async def get_posts(session: AsyncSession):
    statement = select(Post)
    result = await session.exec(statement)
    return result.all()

async def create_post(session: AsyncSession, post: Post):
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post

async def get_post(session: AsyncSession, post_id: int):
    return await session.get(Post, post_id)

async def delete_post(session: AsyncSession, post_id: int):
    post = await session.get(Post, post_id)
    if post:
        await session.delete(post)
        await session.commit()
    return post

async def update_post(session: AsyncSession, post_id: int, post_data: Post):
    post = await session.get(Post, post_id)
    if post:
        post.title = post_data.title
        post.content = post_data.content
        await session.commit()
        await session.refresh(post)
    return post