from src.services import QuizzService


service = QuizzService()

def obterQuizz(quantidade = None, assunto = None):
    qnt = int(quantidade) if quantidade else 10
    
    quizzes = service.obterQuizzes(qnt, assunto)
    return [quiz.__dict__ for quiz in quizzes]
