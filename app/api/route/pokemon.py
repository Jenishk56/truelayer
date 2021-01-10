from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from
from app.api.model.pokemon import PokemonModel
from app.api.schema.pokemon import PokemonSchema

pokemon_api = Blueprint('api', __name__)


@pokemon_api.route('/')
def home():
    result = "Sorry, the given request is not available! Please try with /pokemon/pokemon_name"
    return result, 404

@pokemon_api.route('/<pokemon>/')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'APIs for pokemon as per Shakespear.',
            'schema': PokemonSchema
        }
    }
})
def getPokemonDescr(pokemon):
    try:
        result = PokemonModel(pokemon)
        return PokemonSchema().dump(result), 200
    except:
        result = "Sorry, the given request is not available! Please try finding something else."
        return result, 404