from typing import Any

from peewee import (
    AutoField,
    CharField,
    ForeignKeyField,
    Model,
    PrimaryKeyField,
    SqliteDatabase,
)

from api_users.models import APIUser
from database.db_config import db
from locations.models import Location


class Device(Model):
    id = AutoField()
    type = CharField()
    login = CharField()
    password = CharField()
    location_id = ForeignKeyField(Location, backref="devices")
    api_user_id = ForeignKeyField(APIUser, backref="devices")

    def to_dict(self) -> dict[str, Any]:
        return self.__data__

    class Meta:
        database = db
        table_name = "devices"
