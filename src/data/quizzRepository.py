import pymongo
from src.configurations.mongoConfiguration import MongoConfiguration

from src.data import Repository
from src.data.mapper.quizzMapper import map_to_dictionary, map_to_entity
from src.models.quizz import Quizz


class QuizzRepository(Repository):
    def __init__(self):
        configs = MongoConfiguration.GetAll('development.env')
        
        client = pymongo.MongoClient(configs['connstring'])
        dbName = configs['database']

        if dbName is not None:
            self.db = client[dbName]
    
    def ObterTodos(self, qnt = 10, filter = None):
        collection = self.db['Quizz']
        result = []
        quizzList = []

        if filter:
            result = collection.find({ "Assunto": filter }).limit(qnt)
        else:
            result = collection.find().limit(qnt)

        for item in result:
            quizzList.append(map_to_entity(item))
        
        return quizzList
        
    def Salvar(self, entidade: Quizz):
        collection = self.db['Quizz']
        collection.insert_one(map_to_dictionary(entidade))