from abc import abstractmethod, ABC
from generic_dao import GenericDAO


class DocumentDAO(GenericDAO, ABC):
    @abstractmethod
    def get_documents_by_something(self, something):
        pass
