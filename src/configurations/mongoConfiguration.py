import os
from dotenv import load_dotenv


class MongoConfiguration:
    @staticmethod
    def GetAll(envName):
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(curr_dir, '..', '..'))
        
        env_path = os.path.join(project_root, 'env', envName)
        
        load_dotenv(env_path)
        db_connstring = os.getenv('MONGO_CONNSTRING')
        
        return { 'connstring' : db_connstring }