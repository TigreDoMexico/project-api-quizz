from dataclasses import dataclass
from src.models.answer import Answer

@dataclass
class Quizz:
    Pergunta: str
    Respostas: list[Answer]
    Assunto: str
    
    def __init__(self, pergunta, respostas, assunto = None):
        self.Pergunta = pergunta
        self.Respostas = respostas
        self.Assunto = assunto if assunto else 'diversos'