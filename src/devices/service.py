from dataclasses import dataclass
from typing import Any

from devices.repository import DeviceRepository
from devices.schemas import DeviceCreate, DeviceResponse, DeviceUpdate


@dataclass
class DeviceService:
    repository: DeviceRepository

    async def get_all(self) -> list[DeviceResponse]:
        db_records = self.repository.get_all()
        dto = [DeviceResponse.model_validate(record.to_dict()) for record in db_records]
        return dto

    async def get_by_id(self, id: int) -> DeviceResponse:
        db_record = self.repository.get_by_id(id)
        dto = DeviceResponse.model_validate(db_record.to_dict())
        return dto

    async def create(self, data: DeviceCreate) -> int:
        flat_data = data.model_dump()
        response = self.repository.create(flat_data)
        return response

    async def update(self, id: int, data: DeviceUpdate) -> DeviceResponse:
        db_record = self.repository.get_by_id(id)
        flat_data = data.model_dump(exclude_unset=True)
        self.repository.update(db_record, flat_data)
        dto = DeviceResponse.model_validate(db_record.to_dict())
        return dto

    async def delete(self, id: int) -> None:
        db_record = self.repository.get_by_id(id)
        self.repository.delete(db_record)
