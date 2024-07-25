from typing import Any

from peewee import AutoField, CharField, Model

from database.db_config import db


class APIUser(Model):
    id = AutoField(primary_key=True)
    name = CharField()
    email = CharField()
    password = CharField()

    def to_dict(self) -> dict[str, Any]:
        return self.__data__

    class Meta:
        database = db
        table_name = "api_users"
