from sqlmodel import SQLModel, Field
from typing import Optional


class Post(SQLModel, table=True):
    __tablename__ = "posts" 
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True, max_length=255)
    content: str
    published: bool = Field(default=True)


# # Example of how to use the Post model
    # class Post(BaseModel):
#     id: Optional[int] = None
#     title: str
#     content: str 
#     published: bool = True
  