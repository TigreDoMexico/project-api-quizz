import boto3
from src.data import repository
from src.models.quizz import Quizz


class QuizzDynamoRepository(repository):
    def __init__(self):
        self.db = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
    
    def ObterTodos(self, qnt = 10, filter = None):
        print('Obter Todos')
        
    def Salvar(self, entidade: Quizz):
        print('Salvar')