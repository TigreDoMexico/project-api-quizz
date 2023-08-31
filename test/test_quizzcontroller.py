from unittest import TestCase
from unittest.mock import MagicMock
import unittest

from src.controllers import QuizzController
from src.services import QuizzService
from src.models import Quizz, Answer


class QuizzControllerTest(TestCase):
    def test_Quando_ObterQuizzes_SemPassarQuantidadeEAssunto_Deve_ChamarServicePassandoQuantidade10(self):
        service = self._mockService()
        controller = QuizzController(service)
        controller.ObterQuizzes()
        
        service.obterQuizzes.assert_called_with(10, None)
        
    def test_Quando_ObterQuizzes_PassandoQuantidadeEAssunto_Deve_ChamarServicePassandoValoresCorrespondentes(self):
        quantidade = '5'
        assunto = 'XPTO'
        
        service = self._mockService()
        controller = QuizzController(service)
        controller.ObterQuizzes(quantidade, assunto)
        
        service.obterQuizzes.assert_called_with(int(quantidade), assunto)
    
    def test_Quando_ObterQuizzes_PassandoSoQuantidadeSemAssunto_Deve_ChamarServicePassandoQuantidade10_EAssuntoPassado(self):
        subject = 'XPTO'
        
        service = self._mockService()
        controller = QuizzController(service)
        controller.ObterQuizzes(assunto=subject)
        
        service.obterQuizzes.assert_called_with(10, subject)
        
    def test_Quando_ObterQuizzes_PassandoQuantidadeSemAssunto_Deve_ChamarServicePassandoQuantidadePassada_ESemAssunto(self):
        qnt = '5'
        
        service = self._mockService()
        controller = QuizzController(service)
        controller.ObterQuizzes(quantidade=qnt)
        
        service.obterQuizzes.assert_called_with(int(qnt), None)

    def test_Dado_UmaRequestCompleta_Quando_ObterQuizzes_Deve_ChamarServicePassandoAsInformacoes(self):
        pergunta = "XPTO"
        assunto = "ABCD"
        respostas = [("RESP1", True), ("RESP2", False), ("RESP3", False)]
        
        request = self._criarRequestPost(pergunta, assunto, respostas)
        
        service = self._mockService()
        controller = QuizzController(service)
        controller.CriarQuizz(request)
        
        service.salvarQuizz.assert_called_with(pergunta, assunto, respostas)

    def test_Dado_UmaRequestSemAssunto_Quando_ObterQuizzes_Deve_ChamarServicePassandoAssuntoNone(self):
        pergunta = "XPTO"
        respostas = [("RESP1", True), ("RESP2", False), ("RESP3", False)]
        
        request = self._criarRequestPost(pergunta, None, respostas)
        
        service = self._mockService()
        controller = QuizzController(service)
        controller.CriarQuizz(request)
        
        service.salvarQuizz.assert_called_with(pergunta, None, respostas)
    
    def _mockService(self):
        retorno = [Quizz('Pergunta 1', Answer('Resposta', True), 'Assunto 1')]
        
        service = QuizzService()
        service.obterQuizzes = MagicMock(return_value = retorno)
        service.salvarQuizz = MagicMock(return_value = True)

        return service
    
    def _criarRequestPost(self, pergunta = None, assunto = None, respostas = None):
        request = {}

        if pergunta is not None:
            request['pergunta'] = pergunta
        
        if assunto is not None:
            request['assunto'] = assunto
        
        if respostas is not None:
            respostas_list_dict = []
            for item in respostas:
                respostas_list_dict.append({ "resposta": item[0], "correta": item[1] })

            request['respostas'] = respostas_list_dict

        return request

if __name__ == '__main__':
    unittest.main()