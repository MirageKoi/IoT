from pydantic import BaseModel


class DeviceResponse(BaseModel):
    id: int
    type: str
    login: str
    location_id: int
    api_user_id: int


class DeviceCreate(BaseModel):
    type: str
    login: str
    password: str
    location_id: int
    api_user_id: int


class DeviceUpdate(BaseModel):
    type: str | None = None
    login: str | None = None
    password: str | None = None
    location_id: int | None = None
    api_user_id: int | None = None
