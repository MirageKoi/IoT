from aiohttp import web

from .dependecies import init_users_api


def setup_routes(app: web.Application) -> None:
    app.router.add_get("/users", init_users_api().get_all_users)
    app.router.add_get("/users/{id}", init_users_api().get_user_by_id)
    app.router.add_post("/users", init_users_api().create_user)
    app.router.add_put("/users/{id}", init_users_api().update_user)
    app.router.add_delete("/users/{id}", init_users_api().delete_user)
