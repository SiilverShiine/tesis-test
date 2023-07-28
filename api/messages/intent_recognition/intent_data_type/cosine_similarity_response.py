from api.messages.intent_recognition.intent_data_type.intent_generic_response import IntentGenericResponse


class CosineSimilarityResponse(IntentGenericResponse):
    """Concrete class that defines the structure of the response of a cosine similarity intent recognizer."""

    def __init__(self, recognition_status: bool, max_similarity_value: float):
        """
        Constructor.

        :param recognition_status: A boolean value that describes if the intent was recognized.
        :param max_similarity_value: The maximum similarity value.
        """

        self.recognition_status: bool = recognition_status
        self.max_similarity_value: float = max_similarity_value
