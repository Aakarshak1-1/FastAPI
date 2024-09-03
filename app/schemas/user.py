from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    hashed_password: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        from_attributes = True
