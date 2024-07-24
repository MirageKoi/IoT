from utils.repository import PeeWeeRepository

from .models import APIUser


class APIUsersRepository(PeeWeeRepository):
    model = APIUser
