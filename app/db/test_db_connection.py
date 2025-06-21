import asyncio
from sqlalchemy import text
from connection import engine  # ✅ Adjust path if needed

async def test_connection():
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT * FROM posts"))  # ✅ wrapped in text()
            print("✅ Connection successful")
    except Exception as e:
        print("❌ Connection failed:", e)

if __name__ == "__main__":
    asyncio.run(test_connection())
