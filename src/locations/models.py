from typing import Any

from peewee import AutoField, CharField, Model

from database.db_config import db


class Location(Model):
    id = AutoField()
    name = CharField()

    def to_dict(self) -> dict[str, Any]:
        return self.__data__

    class Meta:
        database = db
        table_name = "locations"
