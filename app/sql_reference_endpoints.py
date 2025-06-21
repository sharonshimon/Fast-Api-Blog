# --- SQL-based endpoints for reference purposes only ---
# This file demonstrates how to use psycopg3 directly instead of SQLModel.
# It is just for reference and learning purposes, not for production use.
# You can see how to perform CRUD operations with psycopg3's async API.

from fastapi import APIRouter
from psycopg import rows
from fastapi import FastAPI


# Example: GET all posts using raw SQL and psycopg3
async def get_posts_sql(app: FastAPI):
    async with app.state.db_pool.connection() as conn:
        conn.row_factory = rows.dict_row
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM posts")
            posts = await cur.fetchall()
    return {"data": posts}



async def create_post(post: Post):
    # This is just for reference: shows how to use psycopg3 for inserts
    if not post.title or not post.content:
        raise HTTPException(status_code=400, detail="Title and content are required")
    
    async with app.state.db_pool.connection() as conn:
        conn.row_factory = rows.dict_row
        async with conn.cursor() as cur:
            await cur.execute(
                """
                INSERT INTO posts (title, content, published)
                VALUES (%s, %s, %s)
                RETURNING *
                """,
                (post.title, post.content, post.published)
            )
            new_post = await cur.fetchone()

    return {"message": "Post created successfully", "post": new_post}

async def get_post(id: int, response: Response):
    # Reference: psycopg3 select by id
    async with app.state.db_pool.connection() as conn:
        conn.row_factory = rows.dict_row
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM posts WHERE id = %s", (id,))
            post = await cur.fetchone()
        if not post:
            raise HTTPException(status_code=404, detail=f"Post with ID {id} not found")
    return {"data": post}

async def delete_post(id: int , status_code: int = 204):
    # Reference: psycopg3 delete by id
    async with app.state.db_pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute("DELETE FROM posts WHERE id = %s RETURNING *", (id,))
            deleted = await cur.fetchone()
        if not deleted:
            raise HTTPException(status_code=404, detail=f"Post with ID {id} not found")
    return {"message": "Post deleted successfully", "post": deleted}

async def update_post(id: int, post: Post):
    # Reference: psycopg3 update by id
    async with app.state.db_pool.connection() as conn:
        conn.row_factory = rows.dict_row
        async with conn.cursor() as cur:
            await cur.execute(
                """
                UPDATE posts
                SET title = %s, content = %s, published = %s
                WHERE id = %s
                RETURNING *
                """,
                (post.title, post.content, post.published, id)
            )
            post = await cur.fetchone()
        if not post:
            raise HTTPException(status_code=404, detail=f"Post with ID {id} not found")
    return {"data": post}

