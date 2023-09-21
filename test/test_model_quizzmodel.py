from unittest import TestCase
import unittest

from src.models import Quizz, Answer


class QuizzModelTest(TestCase):
    def test_Quando_CriarNovoQuizz_SemPassarAssunto_Deve_PreeencherAssuntoComDiversos(self):
        novoQuizz = Quizz('PerguntaX', self._criarRespostasPraPergunta())
        
        self.assertEqual(novoQuizz.Assunto, 'diversos')
        
    def test_Quando_CriarNovoQuizz_PassandoAssunto_Deve_PreeencherAssuntoComValorPassado(self):
        assunto = 'XPTO'
        novoQuizz = Quizz('PerguntaX', self._criarRespostasPraPergunta(), assunto)
        
        self.assertEqual(novoQuizz.Assunto, assunto)
        
    def _criarRespostasPraPergunta(self):
        return [Answer('RESPOSTA1', True)]

if __name__ == '__main__':
    unittest.main()