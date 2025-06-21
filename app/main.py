import os
from random import randrange
from typing import Optional

from contextlib import asynccontextmanager
from fastapi import FastAPI

from db.connection import init_db
from routers.post import router as post_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🔄 Initializing DB...")
    await init_db()  
    yield
    print("🛑 Lifespan ended. Clean up if needed.")



app = FastAPI(lifespan=lifespan)

# Main API routers
app.include_router(post_router)

# --- SQL-based endpoints for reference are now in sql_reference_endpoints.py ---
# They are not included in the main app by

