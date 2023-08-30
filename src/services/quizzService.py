from src.models import Quizz, Answer


class QuizzService:
    def __init__(self, quizzes = None) -> None:
        self.lista_quizzes = quizzes if quizzes else []
    
    def obterQuizzes(self, quantidade:int = 10, assunto:str | None = None) -> list[Quizz]:
        elementos_com_assunto = self.lista_quizzes
        
        if(assunto):
            elementos_com_assunto = [quizz for quizz in self.lista_quizzes if quizz.Assunto == assunto]
            
        return elementos_com_assunto[:quantidade]

    def salvarQuizz(self, quizz: Quizz) -> bool:
        self.lista_quizzes.append(quizz)

    def obterQuizzPorId(self, id) -> Quizz:
        return next((x for x in self.lista_quizzes if x.Id == id), None)
        