from nltk.corpus import stopwords
from unidecode import unidecode

from api.data_builder.base_data_builder import BaseDataBuilder


class StopWordsCleaner(BaseDataBuilder):
    """Concrete data builder that removes stop words from each data phrase."""

    def build_data(self, data: list[str]) -> list[str]:
        """
        Process the data set to remove irrelevant symbols, remove tildes and converts characters to lowercase.

        :param data: The data set that will be processed by the current builder data.
        """

        built_data: list[str] = []

        # Define stopwords in Spanish
        stopwords_es = set(stopwords.words('spanish'))
        stopwords_es_cleaned = set(unidecode(word) for word in stopwords_es)

        for data_phrase in data:
            built_data.append(' '.join(word for word in data_phrase.split() if word not in stopwords_es_cleaned))

        return super().build_data(built_data)
