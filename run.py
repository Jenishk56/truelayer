from flask import Flask
from flasgger import Swagger
from app.api.route.pokemon import pokemon_api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(pokemon_api, url_prefix='/pokemon')
    return app

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)
