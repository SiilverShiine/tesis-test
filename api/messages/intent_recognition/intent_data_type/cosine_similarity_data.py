from api.messages.intent_recognition.intent_data_type.intent_generic_data_type import IntentGenericDataType


class CosineSimilarityData(IntentGenericDataType):
    """Concrete class that defines the structure of the object data needed by a cosine similarity intent recognizer."""

    def __init__(self, user_message: str, training_data: list[str]):
        """
        Constructor.

        :param user_message: The message sent by the user.
        :param training_data: Group of phrases to be used to calculate cosine similarity.
        """

        self.user_message: str = user_message
        self.training_data: list[str] = training_data
