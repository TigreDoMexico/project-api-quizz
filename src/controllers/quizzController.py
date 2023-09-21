from src.services import QuizzService


class QuizzController:
    def __init__(self, service = None):
        self.Service = service if service else QuizzService()
        
    def ObterQuizzes(self, quantidade = None, assunto: str | None = None):
        qnt = int(quantidade) if quantidade else 10
    
        quizzes = self.Service.obterQuizzes(qnt, assunto)
        return [quiz.__dict__ for quiz in quizzes]
    
    def CriarQuizz(self, request):
        listaRespostas = []
        
        pergunta = request.get('pergunta')
        assunto = request.get('assunto')
        respostas = request.get('respostas')

        for item in respostas:
            resposta = item.get('resposta')
            correta = item.get('correta')
            listaRespostas.append((resposta, correta))

        self.Service.salvarQuizz(pergunta, assunto, listaRespostas)