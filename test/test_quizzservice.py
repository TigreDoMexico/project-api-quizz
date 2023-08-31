from unittest import TestCase

from src.services import QuizzService
from src.models import Quizz, Answer


class QuizzServiceTest(TestCase):
    QuantidadePadrao = 10
    
    def test_Dado_UmaListaDeQuizzes_Quando_ObterQuizzes_NaoPassandoNada_Deve_Retornar10ItensComAssuntosDiversos(self):
        service = QuizzService(self._criarListaQuizzes())
        retorno = service.obterQuizzes()
        
        self.assertEqual(len(retorno), self.QuantidadePadrao)
        
    def test_Dado_UmaListaDeQuizzes_Quando_ObterQuizzes_PassandoUmaQuantidadeMaiorQueOsDados_Deve_RetornarOTotalDeItensSalvosComAssuntoDiverso(self):
        quantidadeRepositorio = 6
        quantidadeRequisitada = 10
        
        service = QuizzService(self._criarListaQuizzes(quantidadeRepositorio))
        retorno = service.obterQuizzes(quantidadeRequisitada)
        
        self.assertEqual(len(retorno), quantidadeRepositorio)
    
    def test_Dado_UmaListaDeQuizzes_Quando_ObterQuizzes_PassandoUmAssunto_Deve_RetornarOTotalDeItensSalvosComAqueleAssunto(self):
        subject = 'XPTO'
        lista_com_assunto = self._criarListaQuizzes(3, subject)
        lista_com_outros_assuntos = self._criarListaQuizzes(7)
        
        service = QuizzService(lista_com_outros_assuntos + lista_com_assunto)
        retorno = service.obterQuizzes(assunto = subject)
        
        self.assertEqual(retorno, lista_com_assunto)
        
    def test_Dado_UmaListaDeQuizzes_Quando_ObterQuizzes_PassandoUmAssuntoQueNaoExiste_Deve_RetornarUmaListaVazia(self):
        subject = 'XPTO'
        
        service = QuizzService(self._criarListaQuizzes(10))
        retorno = service.obterQuizzes(assunto = subject)
        
        self.assertIsNotNone(retorno)
        self.assertEqual(len(retorno), 0)

    def test_Dado_UmQuizzParaCriar_Quando_SalvarQuizz_ComInformacoesCorretas_Deve_RetornarTrue_E_SalvarNaLista(self):
        pergunta = 'XPTO?'
        assunto = 'ABCD'
        respostas = [('Resposta 1', True), ('Resposta 2', False), ('Resposta 3', False)]
        
        service = QuizzService()
        retorno = service.salvarQuizz(pergunta, assunto, respostas)
        
        self.assertTrue(retorno)
        self.assertEqual(len(service.lista_quizzes), 1)

    def test_Dado_UmQuizzParaCriar_Quando_SalvarQuizz_ComDuasRepostasCertas_Deve_RetornarFalse_E_NaoSalvarNaLista(self):
        pergunta = 'XPTO?'
        assunto = 'ABCD'
        respostas = [('Resposta 1', True), ('Resposta 2', True), ('Resposta 3', False)]
        
        service = QuizzService()
        retorno = service.salvarQuizz(pergunta, assunto, respostas)
        
        self.assertFalse(retorno)
        self.assertEqual(len(service.lista_quizzes), 0)

    def test_Dado_UmQuizzParaCriar_Quando_SalvarQuizz_SemRespostas_Deve_RetornarFalse_E_NaoSalvarNaLista(self):
        pergunta = 'XPTO?'
        assunto = 'ABCD'
        respostas = []
        
        service = QuizzService()
        retorno = service.salvarQuizz(pergunta, assunto, respostas)
        
        self.assertFalse(retorno)
        self.assertEqual(len(service.lista_quizzes), 0)
    
    def test_Dado_UmQuizzParaCriar_Quando_SalvarQuizz_SemRespostas_Deve_RetornarTrue_E_SalvarQuizzComAssuntoDiversos(self):
        pergunta = 'XPTO?'
        assunto = None
        respostas = [('Resposta 1', True), ('Resposta 2', False), ('Resposta 3', False)]
        
        service = QuizzService()
        retorno = service.salvarQuizz(pergunta, assunto, respostas)
        
        self.assertTrue(retorno)
        self.assertEqual(service.lista_quizzes[0].Assunto, 'diversos')
        
    def _criarListaQuizzes(self, quantidade = 10, assunto = None):
        repositorio = []
        for i in range(quantidade):
            quizz = Quizz(f'Pergunta {i}', Answer('Resposta', True), assunto if assunto else f'Assunto {i}')
            repositorio.append(quizz)
            
        return repositorio