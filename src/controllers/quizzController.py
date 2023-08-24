from src.models.answer import Answer
from src.models.quizz import Quizz

def obterQuizz():
    answer1 = Answer('Elisabeth', True)
    answer2 = Answer('Martha', False)
    answer3 = Answer('Mary Jane', False)
    
    quizz = Quizz('Quem foi a rainha da Inglaterra', [answer1, answer2, answer3])
    return quizz