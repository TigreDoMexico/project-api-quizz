from src.services import QuizzService


class QuizzController:
    def __init__(self, service = None):
        self.Service = service if service else QuizzService()
        
    def ObterQuizzes(self, quantidade = None, assunto = None):
        qnt = int(quantidade) if quantidade else 10
    
        quizzes = self.Service.obterQuizzes(qnt, assunto)
        return [quiz.__dict__ for quiz in quizzes]
    
    def CriarQuizzes(self, quizz):
        print("TODO")
        #quizzes = self.Service.salvarQuizz(qnt, assunto)
        #return [quiz.__dict__ for quiz in quizzes]