from dataclasses import dataclass

from aiohttp import web

from api_users.schemas import APIUserCreate, APIUserUpdate

from .service import APIUsersService


@dataclass
class APIUsersAPI:
    service: APIUsersService

    async def get_all_users(self, request: web.Request) -> web.Response:
        dto = await self.service.get_all()
        response = [obj.model_dump() for obj in dto]
        return web.json_response(response)

    async def get_user_by_id(self, request: web.Request) -> web.Response:
        _id = int(request.match_info["id"])
        dto = await self.service.get_by_id(_id)
        response = dto.model_dump()
        return web.json_response(response)

    async def create_user(self, request: web.Request) -> web.Response:
        request_body = await request.post()
        validated_data = APIUserCreate.model_validate(request_body)
        response = await self.service.create(validated_data)
        return web.json_response(text=f"Success. User with id: {response} has been created", status=201)

    async def update_user(self, request: web.Request) -> web.Response:
        _id = int(request.match_info["id"])
        request_body = await request.post()
        validated_data = APIUserUpdate.model_validate(request_body)
        dto = await self.service.update(_id, validated_data)
        response = dto.model_dump()
        return web.json_response(response)

    async def delete_user(self, request: web.Request):
        _id = int(request.match_info["id"])
        await self.service.delete(_id)
        return web.json_response(text="Success", status=204)
