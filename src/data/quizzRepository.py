import pymongo
from src.configurations.mongoConfiguration import MongoConfiguration

from src.data import Repository
from src.models.quizz import Quizz


class QuizzRepository(Repository):
    def __init__(self):
        configs = MongoConfiguration.GetAll('development.env')
        
        client = pymongo.MongoClient(configs['connstring'])
        self.db = client[configs['database']]
    
    def ObterTodos(self, qnt = 10, filter = None):
        collection = self.db['Quizz']
        result = []
        quizzList = []

        if filter:
            result = collection.find({ "Assunto": filter }).limit(qnt)
        else:
            result = collection.limit(qnt)

        for item in result:
            quizzList.append(Quizz.to_class(item))
        
        return quizzList
        
    def Salvar(self, entidade):
        collection = self.db['Quizz']
        collection.insert_one(entidade)