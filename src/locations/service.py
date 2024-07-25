from dataclasses import dataclass

from locations.repository import LocationRepository
from locations.schemas import LocationCreate, LocationResponse


@dataclass
class LocationService:
    repository: LocationRepository

    async def get_all(self) -> list[LocationResponse]:
        db_records = await self.repository.get_all()
        dto = [LocationResponse.model_validate(record.to_dict()) for record in db_records]
        return dto

    async def create(self, data: LocationCreate) -> int:
        return self.repository.create(data.model_dump())

    async def delete(self, id: int) -> None:
        db_record = self.repository.get_by_id(id)
        return self.repository.delete(db_record)
