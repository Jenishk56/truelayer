from unittest import TestCase
from run import create_app


class Test_Pokemon(TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_pokemon_with_name(self):
        """
        Tests the actual pokemon api
        """
        result = self.app.get('/pokemon/charizard/')
        get_json = result.get_json()
        if get_json != None:
            message = get_json["message"]
            # Check assertion on message
            self.assertTrue(message)
        else:
            self.assertEqual("json", "failed")

    def test_pokemon_without_name(self):
        """
        Tests the actual pokemon api
        """
        result = self.app.get('/pokemon/')
        get_data = result.get_data()
        assert b'Sorry, the given request is not available! Please try with /pokemon/pokemon_name' in get_data
        
