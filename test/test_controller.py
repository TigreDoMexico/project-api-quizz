from unittest import TestCase
import unittest

from src.controllers import obterQuizz


class ControllerTest(TestCase):
    def test_Quando_ObterQuizzes_SemPassarQuantidadeEAssunto_Deve_RetornarDezElementosComAssuntosDiversos(self):
        retorno = obterQuizz()
        
        self.assertEqual(len(retorno), 10)
        self.assertEqual(retorno[0].Pergunta, 'diversos')
        
    def test_Quando_ObterQuizzes_ComQuantidadeDoisESemAssunto_Deve_RetornarDoisElementosComAssuntosDiversos(self):
        quantidade = 2
        retorno = obterQuizz(quantidade)
        
        self.assertEqual(len(retorno), quantidade)
        self.assertEqual(retorno[0].Pergunta, 'diversos')
    
    def test_Quando_ObterQuizzes_ComAssuntoESemQuantidade_Deve_RetornarDezElementosComAssuntoInformado(self):
        subject = 'XPTO'
        retorno = obterQuizz(assunto = subject)
        
        self.assertEqual(len(retorno), 10)
        self.assertEqual(retorno[0].Pergunta, subject)
        
    def test_Quando_ObterQuizzes_ComQuantidadeEAssunto_Deve_RetornarAQuantidadeDeElementosPedidaComOAssuntoInformado(self):
        quantidade = 5
        assunto = 'XPTO'
        retorno = obterQuizz(quantidade, assunto)
        
        self.assertEqual(len(retorno), quantidade)
        self.assertEqual(retorno[0].Pergunta, assunto)

if __name__ == '__main__':
    unittest.main()