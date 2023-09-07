from unittest import TestCase
from src.data.mapper.quizzMapper import map_to_dictionary, map_to_entity
from src.models import Quizz, Answer


class QuizzMapperTest(TestCase):
    def test_Dado_UmQuizz_Quando_MapearParaDictionary_Deve_RetornarUmDictionaryCorreto(self):
        pergunta = 'PERGUNTA ?'
        assunto = 'ASSUNTO'
        respostas = [Answer('Resposta 1', True), Answer('Resposta 2', False), Answer('Resposta 3', False)]
        
        entidade = Quizz(pergunta, respostas, assunto)
        
        resultado = map_to_dictionary(entidade)
        
        self.assertEqual(resultado, {
            'Pergunta' : pergunta,
            'Assunto': assunto,
            'Respostas': [
                {
                    'Texto': respostas[0].Texto,
                    'Correto': respostas[0].Correto
                },
                {
                    'Texto': respostas[1].Texto,
                    'Correto': respostas[1].Correto
                },
                {
                    'Texto': respostas[2].Texto,
                    'Correto': respostas[2].Correto
                }
            ]
        })
        
    def test_Dado_UmDicionario_Quando_MapearParaEntidade_Deve_RetornarUmaQuizzComRepostas(self):
        pergunta = 'PERGUNTA ?'
        assunto = 'ASSUNTO'
        respostas = [Answer('Resposta 1', True), Answer('Resposta 2', False), Answer('Resposta 3', False)]
        
        dicionario = {
            'Pergunta' : pergunta,
            'Assunto': assunto,
            'Respostas': [
                {
                    'Texto': respostas[0].Texto,
                    'Correto': respostas[0].Correto
                },
                {
                    'Texto': respostas[1].Texto,
                    'Correto': respostas[1].Correto
                },
                {
                    'Texto': respostas[2].Texto,
                    'Correto': respostas[2].Correto
                }
            ]
        }
        
        resultado = map_to_entity(dicionario)
        
        self.assertEqual(resultado, Quizz(pergunta, respostas, assunto))