from unittest import TestCase
from unittest.mock import MagicMock
import unittest

from src.controllers import QuizzController
from src.services import QuizzService
from src.models import Quizz, Answer


class QuizzControllerTest(TestCase):
    def test_Quando_ObterQuizzes_SemPassarQuantidadeEAssunto_Deve_ChamarServicePassandoQuantidade10(self):
        service = self._mockService(10)
        controller = QuizzController(service)
        controller.ObterQuizzes()
        
        service.obterQuizzes.assert_called_with(10, None)
        
    def test_Quando_ObterQuizzes_PassandoQuantidadeEAssunto_Deve_ChamarServicePassandoValoresCorrespondentes(self):
        quantidade = '5'
        assunto = 'XPTO'
        
        service = self._mockService(10)
        controller = QuizzController(service)
        controller.ObterQuizzes(quantidade, assunto)
        
        service.obterQuizzes.assert_called_with(int(quantidade), assunto)
    
    def test_Quando_ObterQuizzes_PassandoSoQuantidadeSemAssunto_Deve_ChamarServicePassandoQuantidade10_EAssuntoPassado(self):
        subject = 'XPTO'
        
        service = self._mockService(10)
        controller = QuizzController(service)
        controller.ObterQuizzes(assunto=subject)
        
        service.obterQuizzes.assert_called_with(10, subject)
        
    def test_Quando_ObterQuizzes_PassandoQuantidadeSemAssunto_Deve_ChamarServicePassandoQuantidadePassada_ESemAssunto(self):
        qnt = '5'
        
        service = self._mockService(10)
        controller = QuizzController(service)
        controller.ObterQuizzes(quantidade=qnt)
        
        service.obterQuizzes.assert_called_with(int(qnt), None)
    
    def _mockService(self, quantidadeDados = 1):
        service = QuizzService()
        
        retorno = []
        for i in range(quantidadeDados):
            quizz = Quizz(f'Pergunta {i}', Answer('Resposta', True), f'Assunto {i}')
            retorno.append(quizz)
        
        service.obterQuizzes = MagicMock(return_value = retorno)
        return service

if __name__ == '__main__':
    unittest.main()