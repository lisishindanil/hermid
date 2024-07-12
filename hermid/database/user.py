from tortoise import Model
from tortoise.fields import (
    BigIntField,
    CharField,
    DatetimeField
)


class User(Model):
    id = BigIntField(pk=True)
    uid = BigIntField(null=False)
    name = CharField(max_length=255, null=False)
    surname = CharField(max_length=255, null=True)
    country_code = CharField(max_length=3, null=True)
    city = CharField(max_length=255, null=True)

    last_activity = DatetimeField(auto_now=True)
