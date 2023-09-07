from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def ObterTodos(self, paginacao, filtro):
        pass
    
    @abstractmethod
    def Salvar(self, entidade):
        pass