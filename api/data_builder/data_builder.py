from abc import ABC, abstractmethod


class DataBuilder(ABC):
    """Handler class that declares the interface common to all concrete data builders."""

    @abstractmethod
    def set_next_builder(self, data_builder: "DataBuilder"):
        """
        Set the following builder data that will be in charge of building the data.

        :param data_builder: The concrete data builder that will build the data.
        """
        pass

    @abstractmethod
    def build_data(self, data: list[str]) -> list[str]:
        """
        Process the data set.

        :param data: The data set that will be processed by the current builder data.
        :return: The data processed by a particular process.
        """
        pass
