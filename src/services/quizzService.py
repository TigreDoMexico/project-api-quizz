from src.data import QuizzRepository
from src.models import Quizz, Answer


class QuizzService:
    def __init__(self, quizzes = None) -> None:
        self.repositorio = QuizzRepository()
    
    def obterQuizzes(self, quantidade:int = 10, assunto:str = None) -> list[Quizz]:
        return self.repositorio.ObterTodos(quantidade, assunto)

    def salvarQuizz(self, pergunta: str, assunto: str, respostas: list[tuple[str, bool]]) -> bool:
        lista_answers = []
        
        for resposta in respostas:
            lista_answers.append(Answer(resposta[0], resposta[1]))

        total_respostas_certas = sum(answer.Correto for answer in lista_answers)

        if(total_respostas_certas == 1):
            entidade = Quizz(pergunta, lista_answers, assunto)
            self.repositorio.Salvar(entidade)
        else:
            return False

        return True
        