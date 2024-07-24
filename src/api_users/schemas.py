from pydantic import BaseModel


class APIUserResponse(BaseModel):
    id: int
    name: str
    email: str


class APIUserCreate(BaseModel):
    name: str
    email: str
    password: str


class APIUserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    password: str | None = None
