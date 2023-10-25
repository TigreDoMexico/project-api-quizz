from src.models import Quizz, Answer


def map_to_dictionary(quizz: Quizz):
    dict = quizz.__dict__
    respostas = [resp.__dict__ for resp in quizz.Respostas]

    dict['Respostas'] = respostas

    return dict

def map_to_entity(dictionary: dict):
    pergunta = dictionary.get('Pergunta')
    assunto = dictionary.get('Assunto')
    dict_respostas = dictionary.get('Respostas')

    respostas = []

    if dict_respostas is not None:
        respostas = [Answer(item.get('Texto'), item.get('Correto')) for item in dict_respostas]

    return Quizz(pergunta, respostas, assunto)