from abc import abstractmethod

from api.messages.intent_recognition.intent_recognizer import IntentRecognizer
from api.messages.intent_recognition.intent_data_type.intent_generic_data_type import IntentGenericDataType


class IntentRecognizerFactory:

    def process_user_intent(self, intent_data: IntentGenericDataType):
        """
        Create a generic intent recognizer and process the user intent.

        :param intent_data: Object with the data needed for the intent recognizer to get the user intent.
        :return: An object representing the user intent.
        """

        intent_recognizer: IntentRecognizer = self.create_recognizer()
        return intent_recognizer.get_user_intent(intent_data)

    @abstractmethod
    def create_recognizer(self) -> IntentRecognizer:
        """
        Create a recognizer based on a specific process.

        :return: A cosine similarity based a specific process.
        """
        pass
