from abc import ABC, abstractmethod

from api.messages.intent_recognition.intent_data_type.intent_generic_response import IntentGenericResponse
from api.messages.intent_recognition.intent_data_type.intent_generic_data_type import IntentGenericDataType


class IntentRecognizer(ABC):
    """Interface that is common to all objects that the intent recognizer factory can produce."""

    @abstractmethod
    def get_user_intent(self, intent_data: IntentGenericDataType) -> IntentGenericResponse:
        """
        Process the user message to determine the intent.

        :param intent_data: Object with the data needed for the intent recognizer to get the user intent.
        :return: An object representing the user intent.
        """
        pass
