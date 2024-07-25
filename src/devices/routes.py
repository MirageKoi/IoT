from aiohttp import web

from .dependecies import init_device_api


def setup_routes(app: web.Application):
    app.router.add_get("/devices", init_device_api().get_all_devices)
    app.router.add_get("/devices/{id}", init_device_api().get_device_by_id)
    app.router.add_post("/devices", init_device_api().create_device)
    app.router.add_put("/devices/{id}", init_device_api().update_device)
    app.router.add_delete("/devices/{id}", init_device_api().delete_device)
