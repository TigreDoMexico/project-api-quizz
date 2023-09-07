from unittest import TestCase
from unittest.mock import MagicMock
from src.data import QuizzRepository

from src.services import QuizzService
from src.models import Quizz, Answer


class QuizzServiceTest(TestCase):
    QuantidadePadrao = 10
    
    def test_Quando_ObterQuizzes_NaoPassandoNada_Deve_ChamarRepositorioPassando10ESemAssunto(self):
        repositorio = self._mockRepositoryComObterTodos()
        service = QuizzService(repositorio)
        
        service.obterQuizzes()
        
        repositorio.ObterTodos.assert_called_once_with(self.QuantidadePadrao, None)
    
    def test_Quando_ObterQuizzes_PassandoUmAssunto_Deve_ChamarRepositorioPassandoOAssunto(self):
        subject = 'XPTO'
        repositorio = self._mockRepositoryComObterTodos()
        
        service = QuizzService(repositorio)
        service.obterQuizzes(assunto = subject)
        
        repositorio.ObterTodos.assert_called_once_with(self.QuantidadePadrao, subject)
    
    def test_Dado_UmQuizzParaCriar_Quando_SalvarQuizz_ComInformacoesCorretas_Deve_EnviarParaRepositoryERetornarTrue(self):
        pergunta = 'XPTO?'
        assunto = 'ABCD'
        respostas = [('Resposta 1', True), ('Resposta 2', False), ('Resposta 3', False)]
        
        respostasSalvas = [Answer(item[0], item[1]) for item in respostas]
        
        repositorio = self._mockRepositoryComSalvar()
        service = QuizzService(repositorio)
        
        retorno = service.salvarQuizz(pergunta, assunto, respostas)
        
        self.assertTrue(retorno)
        repositorio.Salvar.assert_called_once_with(Quizz(pergunta, respostasSalvas, assunto))

    def test_Dado_UmQuizzParaCriar_Quando_SalvarQuizz_ComDuasRepostasCertas_Deve_RetornarFalse_E_NaoSalvarNoRepositorio(self):
        pergunta = 'XPTO?'
        assunto = 'ABCD'
        respostas = [('Resposta 1', True), ('Resposta 2', True), ('Resposta 3', False)]
        
        repositorio = self._mockRepositoryComSalvar()
        service = QuizzService(repositorio)
        
        retorno = service.salvarQuizz(pergunta, assunto, respostas)
        
        self.assertFalse(retorno)
        repositorio.Salvar.assert_not_called()
        
    def test_Dado_UmQuizzParaCriar_Quando_SalvarQuizz_ComNenhumaRepostaCerta_Deve_RetornarFalse_E_NaoSalvarNoRepositorio(self):
        pergunta = 'XPTO?'
        assunto = 'ABCD'
        respostas = [('Resposta 1', False), ('Resposta 2', False), ('Resposta 3', False)]
        
        repositorio = self._mockRepositoryComSalvar()
        service = QuizzService(repositorio)
        
        retorno = service.salvarQuizz(pergunta, assunto, respostas)
        
        self.assertFalse(retorno)
        repositorio.Salvar.assert_not_called()

    def test_Dado_UmQuizzParaCriar_Quando_SalvarQuizz_SemRespostas_Deve_RetornarFalse_E_NaoSalvarNoRepositorio(self):
        pergunta = 'XPTO?'
        assunto = 'ABCD'
        respostas = []
        
        repositorio = self._mockRepositoryComSalvar()
        service = QuizzService(repositorio)
        
        retorno = service.salvarQuizz(pergunta, assunto, respostas)
        
        self.assertFalse(retorno)
        repositorio.Salvar.assert_not_called()
    
    def test_Dado_UmQuizzParaCriar_Quando_SalvarQuizz_SemAssunto_Deve_RetornarTrue_E_SalvarNoRepositorioComAssuntoDiversos(self):
        pergunta = 'XPTO?'
        assunto = None
        respostas = [('Resposta 1', True), ('Resposta 2', False), ('Resposta 3', False)]
        
        respostasSalvas = [Answer(item[0], item[1]) for item in respostas]
        
        repositorio = self._mockRepositoryComSalvar()
        service = QuizzService(repositorio)
        retorno = service.salvarQuizz(pergunta, assunto, respostas)
        
        self.assertTrue(retorno)
        repositorio.Salvar.assert_called_once_with(Quizz(pergunta, respostasSalvas, 'diversos'))
    
    def _mockRepositoryComSalvar(self, retorno = True):
        repository = QuizzRepository()
        repository.Salvar = MagicMock(return_value = retorno)

        return repository
    
    def _mockRepositoryComObterTodos(self, retorno = []):
        repository = QuizzRepository()
        repository.ObterTodos = MagicMock(return_value = retorno)

        return repository