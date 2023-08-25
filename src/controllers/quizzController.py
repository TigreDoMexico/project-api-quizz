from src.models import Answer, Quizz

def obterQuizz(quantidade = 10, assunto = ''):
    lista_quizz = []

    for _ in range(quantidade):
        answer1 = Answer('Resposta A', True)
        answer2 = Answer('Resposta B', False)
        answer3 = Answer('Resposta C', False)
    
        quizz = Quizz(assunto, [answer1, answer2, answer3])
        lista_quizz.append(quizz)
    
    return lista_quizz