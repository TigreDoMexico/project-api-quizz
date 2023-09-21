from src.data import QuizzRepository
from src.models import Quizz, Answer


class QuizzService:
    def __init__(self, repository = None) -> None:
        self.repositorio = repository if repository else QuizzRepository()
    
    def obterQuizzes(self, quantidade:int = 10, assunto:str | None = None):
        return self.repositorio.ObterTodos(quantidade, assunto)

    def salvarQuizz(self, pergunta: str, assunto: str | None, respostas) -> bool:
        lista_answers = [Answer(resposta[0], resposta[1]) for resposta in respostas]
        total_respostas_certas = sum(answer.Correto for answer in lista_answers)

        if(total_respostas_certas == 1):
            entidade = Quizz(pergunta, lista_answers, assunto)
            self.repositorio.Salvar(entidade)
        else:
            return False

        return True
        