import json
import logging

from aiohttp import web

from api_users.models import APIUser
from api_users.routes import setup_routes as setup_users_routes
from database.db_config import db
from devices.models import Device
from devices.routes import setup_routes as setup_devices_routes
from locations.models import Location
from locations.routes import setup_routes as setup_locations_routes


def json_error(status_code: int, exception: Exception) -> web.Response:
    """
    Returns a Response from an exception.
    Used for error middleware.
    :param status_code:
    :param exception:
    :return:
    """
    return web.Response(
        status=status_code,
        body=json.dumps({"error": exception.__class__.__name__, "detail": str(exception)}).encode("utf-8"),
        content_type="application/json",
    )


async def error_middleware(app: web.Application, handler):
    """
    This middleware handles with exceptions received from views or previous middleware.
    :param app:
    :param handler:
    :return:
    """

    async def middleware_handler(request):
        try:
            response = await handler(request)
            if response.status == 404:
                return json_error(response.status, Exception(response.message))
            return response
        except ValueError as ex:
            return json_error(422, ex)

        except web.HTTPException as ex:
            if ex.status in [404, 422]:
                return json_error(ex.status, ex)
            raise
        except Exception as e:
            return json_error(500, e)

    return middleware_handler


async def init_app() -> web.Application:
    db.connect()
    db.create_tables([Device, APIUser, Location])
    db.close()

    app = web.Application(middlewares=[error_middleware])

    setup_users_routes(app)
    setup_devices_routes(app)
    setup_locations_routes(app)

    return app


if __name__ == "__main__":
    app = init_app()
    logging.basicConfig(level=logging.DEBUG)
    web.run_app(app=app)
