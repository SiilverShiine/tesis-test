from abc import abstractmethod, ABC


class GenericDAO(ABC):
    @abstractmethod
    def create(self, entity):
        pass

    @abstractmethod
    def read(self, id):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity):
        pass
