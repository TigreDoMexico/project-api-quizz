from unittest import TestCase

from src.configurations.mongoConfiguration import MongoConfiguration


class MongoConfigurationTest(TestCase):
    def test_Quando_ObterConfiguracaoDoMongo_Deve_RetornarOsDadosCorretos(self):
        config = MongoConfiguration.GetAll('test.env')
        self.assertEqual(config, { 'connstring' :  'mongodb://localhost:12345/', 'database' : 'QuizzDatabase' })