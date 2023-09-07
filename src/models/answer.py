from dataclasses import dataclass

@dataclass
class Answer:
    Texto: str
    Correto: bool
    
    def __init__(self, texto, correto):
        self.Texto = texto
        self.Correto = correto
        