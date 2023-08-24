from dataclasses import dataclass
from models.answer import Answer

@dataclass
class Quizz:
    Pergunta: str
    Respostas: list[Answer]
    
    def __init__(self, pergunta, respostas):
        self.Pergunta = pergunta
        self.Respostas = respostas