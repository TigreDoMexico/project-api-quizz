import pymongo
from src.configurations.mongoConfiguration import MongoConfiguration

from src.data import Repository


class QuizzRepository(Repository):
    def __init__(self):
        configs = MongoConfiguration.GetAll('development.env')
        
        client = pymongo.MongoClient(configs['connstring'])
        self.db = client[configs['database']]
    
    def ObterTodos(self, paginacao, filtro):
        print('TODO')
        
    def Salvar(self, entidade):
        collection = self.db['Quizz']
        collection.insert_one(entidade)