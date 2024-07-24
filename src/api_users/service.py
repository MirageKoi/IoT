from dataclasses import dataclass

from api_users.repository import APIUsersRepository

from .schemas import APIUserCreate, APIUserResponse, APIUserUpdate


@dataclass
class APIUsersService:
    repository: APIUsersRepository

    async def get_all(self) -> list[APIUserResponse]:
        db_records = self.repository.get_all()
        dto = [APIUserResponse.model_validate(record.to_dict()) for record in db_records]
        return dto

    async def get_by_id(self, id: int) -> APIUserResponse:
        db_record = self.repository.get_by_id(id)
        dto = APIUserResponse.model_validate(db_record.to_dict())
        return dto

    async def create(self, data: APIUserCreate) -> int:
        validated_data = data.model_dump()
        response = self.repository.create(validated_data)
        return response

    async def update(self, id: int, data: APIUserUpdate) -> APIUserResponse:
        db_record = self.repository.get_by_id(id)
        response = self.repository.update(db_record, data.model_dump(exclude_unset=True))
        dto = APIUserResponse.model_validate(response.to_dict())
        return dto

    async def delete(self, id: int):
        db_record = self.repository.get_by_id(id)
        self.repository.delete(db_record)
