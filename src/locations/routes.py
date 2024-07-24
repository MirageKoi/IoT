from aiohttp import web

from .dependecies import init_location_api


def setup_routes(app: web.Application) -> None:
    app.router.add_get("/locations", init_location_api().get_all_locations)
    app.router.add_post("/locations", init_location_api().create_location)
    app.router.add_delete("/locations/{id}", init_location_api().delete_location)
