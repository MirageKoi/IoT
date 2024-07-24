from dataclasses import dataclass

from aiohttp import web

from locations.schemas import LocationCreate

from .service import LocationService


@dataclass
class LocationAPI:
    service: LocationService

    async def get_all_locations(self, request: web.Request) -> web.Response:
        dto = await self.service.get_all()
        response = [obj.model_dump() for obj in dto]
        return web.json_response(response)

    async def create_location(self, request: web.Request) -> web.Response:
        request_body = await request.post()
        validated_data = LocationCreate.model_validate(request_body)
        response = await self.service.create(validated_data)
        return web.json_response(text=f"Success. Location with id: {response} has been created", status=201)

    async def delete_location(self, request: web.Request) -> web.Response:
        _id = int(request.match_info["id"])
        await self.service.delete(_id)
        return web.json_response(text="Success", status=204)
