from dataclasses import dataclass

@dataclass
class Quizz:
    Pergunta: str
    Respostas: list
    Assunto: str
    
    def __init__(self, pergunta, respostas, assunto = None):
        self.Pergunta = pergunta
        self.Respostas = respostas
        self.Assunto = assunto if assunto else 'diversos'