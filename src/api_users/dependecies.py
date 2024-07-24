from .api import APIUsersAPI
from .repository import APIUsersRepository
from .service import APIUsersService


def init_users_api():
    return APIUsersAPI(APIUsersService(APIUsersRepository()))
