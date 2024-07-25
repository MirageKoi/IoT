from aiohttp import web
from peewee import DoesNotExist, IntegrityError, Model, ModelSelect
from peewee_async import Manager


class PeeWeeRepository:
    model: type[Model]

    @property
    def objects(self):
        return Manager(self.model._meta.database)

    async def get_all(self) -> list[ModelSelect]:
        return await self.objects.execute(self.model.select())

    async def get_by_id(self, id: int) -> type[Model]:
        try:
            return await self.objects.get(self.model, self.model.id == id)
        except DoesNotExist:
            raise web.HTTPNotFound(reason=f"{self.model.__name__} with {id=} not found")

    async def create(self, data: dict[str, str]) -> int:
        try:
            new_object = await self.objects.execute(self.model.insert(**data))
            return new_object
        except IntegrityError:
            raise web.HTTPUnprocessableEntity()

    async def update(self, db_record: type[Model], data: dict[str, str]):
        try:
            for key, value in data.items():
                setattr(db_record, key, value)
            await self.objects.update(db_record)
            return db_record
        except IntegrityError:
            raise web.HTTPUnprocessableEntity()

    async def delete(self, db_record: type[Model]):
        await self.objects.delete(db_record)
