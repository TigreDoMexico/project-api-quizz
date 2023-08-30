from src.models import Quizz, Answer


class QuizzService:
    def __init__(self, quizzes = None) -> None:
        self.lista_quizzes = quizzes if quizzes else []
    
    def obterQuizzes(self, quantidade:int = 10, assunto:str | None = None) -> list[Quizz]:
        elementos_com_assunto = self.lista_quizzes
        
        if(assunto):
            elementos_com_assunto = [quizz for quizz in self.lista_quizzes if quizz.Assunto == assunto]
            
        return elementos_com_assunto[:quantidade]

    def salvarQuizz(self, pergunta: str, assunto: str, respostas: list[tuple[str, bool]]) -> bool:
        lista_answers = []
        
        for resposta in respostas:
            lista_answers.append(Answer(resposta[0], resposta[1]))

        self.lista_quizzes.append(Quizz(pergunta, lista_answers, assunto))
        return True

    def obterQuizzPorId(self, id) -> Quizz:
        return next((x for x in self.lista_quizzes if x.Id == id), None)
        