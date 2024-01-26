from tortoise.models import Model
from tortoise import fields


class Repository(Model):
    id = fields.BigIntField(pk=True)
    owner_id = fields.BigIntField()
    owner_name = fields.CharField(max_length=255)
    lower_name = fields.CharField(max_length=255)
    name = fields.CharField(max_length=255)
    num_stars = fields.IntField()
    fork_id = fields.BigIntField()
    created_unix = fields.BigIntField()
    updated_unix = fields.BigIntField()


class Action(Model):
    id = fields.BigIntField(pk=True)
    user_id = fields.BigIntField()
    repo_id = fields.BigIntField()
    created_unix = fields.BigIntField()

