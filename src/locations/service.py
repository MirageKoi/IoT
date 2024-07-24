from dataclasses import dataclass

from locations.repository import LocationRepository
from locations.schemas import LocationCreate, LocationResponse


@dataclass
class LocationService:
    repository: LocationRepository

    async def get_all(self) -> list[LocationResponse]:
        db_records = self.repository.get_all()
        return [record.to_dict() for record in db_records]

    async def create(self, data: LocationCreate) -> int:
        return self.repository.create(data.model_dump())

    async def delete(self, id: int) -> None:
        db_record = self.repository.get_by_id(id)
        return self.repository.delete(db_record)
