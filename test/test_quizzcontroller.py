from unittest import TestCase
import unittest

from src.controllers import obterQuizz


class QuizzControllerTest(TestCase):
    def test_Quando_ObterQuizzes_SemPassarQuantidadeEAssunto_Deve_RetornarDezElementos(self):
        retorno = obterQuizz()
        
        self.assertEqual(len(retorno), 10)
        
    def test_Quando_ObterQuizzes_ComQuantidadeDoisESemAssunto_Deve_RetornarDoisElementos(self):
        quantidade = '2'
        retorno = obterQuizz(quantidade)
        
        self.assertEqual(len(retorno), int(quantidade))
    
    def test_Quando_ObterQuizzes_ComAssuntoESemQuantidade_Deve_RetornarDezElementos(self):
        subject = 'XPTO'
        retorno = obterQuizz(assunto = subject)
        
        self.assertEqual(len(retorno), 10)
        
    def test_Quando_ObterQuizzes_ComQuantidadeEAssunto_Deve_RetornarAQuantidadeDeElementosPedida(self):
        quantidade = '5'
        assunto = 'XPTO'
        retorno = obterQuizz(quantidade, assunto)
        
        self.assertEqual(len(retorno), int(quantidade))

if __name__ == '__main__':
    unittest.main()