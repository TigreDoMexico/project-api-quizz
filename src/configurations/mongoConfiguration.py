import os
from dotenv import load_dotenv


class MongoConfiguration:
    @staticmethod
    def GetAll(envName):
        project_root = os.path.join(os.path.dirname(__file__), '..', '..')
        env_path = os.path.join(project_root, 'env', envName)

        load_dotenv(env_path)
        db_connstring = os.getenv('MONGO_CONNSTRING')
        db_name = os.getenv('MONGO_DBNAME')

        return { 'connstring' : db_connstring, 'database' : db_name }