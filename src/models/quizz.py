from dataclasses import dataclass
from src.models.answer import Answer

@dataclass
class Quizz:
    static_id = 0
    
    Id: int
    Pergunta: str
    Respostas: list[Answer]
    Assunto: str
    
    def __init__(self, pergunta, respostas, assunto = None):
        self.Id = Quizz.static_id
        self.Pergunta = pergunta
        self.Respostas = respostas
        self.Assunto = assunto if assunto else 'diversos'
        
        Quizz.static_id += 1