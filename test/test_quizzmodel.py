from unittest import TestCase
import unittest

from src.models import Quizz, Answer


class QuizzModelTest(TestCase):
    def test_Quando_CriarDoisQuizzSeguidos_DevePreeencherIdComOsValoresAdicionados(self):
        novoQuizz1 = Quizz('PerguntaX', self._criarRespostasPraPergunta(), 'AssuntoX')
        novoQuizz2 = Quizz('PerguntaY', self._criarRespostasPraPergunta(), 'AssuntoY')
        
        self.assertEquals(novoQuizz2.Id, novoQuizz1.Id + 1)
        
    def test_Quando_CriarNovoQuizz_SemPassarAssunto_Deve_PreeencherAssuntoComDiversos(self):
        novoQuizz = Quizz('PerguntaX', self._criarRespostasPraPergunta())
        
        self.assertEquals(novoQuizz.Assunto, 'diversos')
        
    def test_Quando_CriarNovoQuizz_PassandoAssunto_Deve_PreeencherAssuntoComValorPassado(self):
        assunto = 'XPTO'
        novoQuizz = Quizz('PerguntaX', self._criarRespostasPraPergunta(), assunto)
        
        self.assertEquals(novoQuizz.Assunto, assunto)
        
    def _criarRespostasPraPergunta(self) -> list[Answer]:
        return [Answer('RESPOSTA1', True)]

if __name__ == '__main__':
    unittest.main()