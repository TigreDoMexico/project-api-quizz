from dataclasses import dataclass

@dataclass
class Answer:
    Texto: str
    Correto: bool
    
    def __init__(self, texto, correto):
        self.Texto = texto
        self.Correto = correto
    
    @staticmethod
    def to_class(dictionary):
        texto = dictionary.get('Texto')
        correto = dictionary.get('Correto')

        return Answer(texto, correto)