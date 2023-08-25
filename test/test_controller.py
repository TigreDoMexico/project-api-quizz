from unittest import TestCase
import unittest

from src.controllers import obterQuizz


class ControllerTest(TestCase):
    def test_Quando_ObterQuizzes_Deve_RetornarDadosCorretos(self):
        retorno = obterQuizz()
        
        self.assertIsNotNone(retorno)

if __name__ == '__main__':
    unittest.main()