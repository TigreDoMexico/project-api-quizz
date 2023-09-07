from src.models.quizz import Quizz, Answer


def map_to_dictionary(quizz: Quizz):
    dict = quizz.__dict__
    respostas = [resp.__dict__ for resp in quizz.Respostas]
        
    dict['Respostas'] = respostas
        
    return dict

def map_to_entity(dictionary: dict):
    respostas = []

    pergunta = dictionary.get('Pergunta')
    assunto = dictionary.get('Assunto')
        
    for item in dictionary.get('Respostas'):
        texto = item.get('Texto')
        correto = item.get('Correto')

        resposta = Answer(texto, correto)
        respostas.append(resposta)

    return Quizz(pergunta, respostas, assunto)