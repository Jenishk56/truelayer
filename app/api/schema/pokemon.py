from flask_marshmallow import Schema
from marshmallow.fields import Str


class PokemonSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ["name","description"]

    message = Str()