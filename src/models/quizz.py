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
    
    def to_dict(self):
        dict = self.__dict__
        respostas = [resp.__dict__ for resp in self.Respostas]
        
        dict['Respostas'] = respostas
        
        return dict
    
    @staticmethod
    def to_class(dictionary):
        respostas = []

        pergunta = dictionary.get('Pergunta')
        assunto = dictionary.get('Assunto')
        
        for item in dictionary.get('Respostas'):
            resposta = Answer.to_class(item)
            respostas.append(resposta)

        return Quizz(pergunta, respostas, assunto)