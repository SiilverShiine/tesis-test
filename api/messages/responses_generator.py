from flask import Request, Response

from api.proxy.proxy_interface import ProxyInterface
from api.data_builder.data_builder import DataBuilder
from api.data_builder.syntax_cleaner import SyntaxCleaner
from api.data_builder.stop_words_cleaner import StopWordsCleaner
from api.data_builder.lemmatizer import Lemmatizer
from api.messages.intent_recognition.intent_recognizer_factory import IntentRecognizerFactory
from api.messages.intent_recognition.cosine_similarity_factory import CosineSimilarityFactory
from api.messages.intent_recognition.intent_data_type.intent_generic_data_type import IntentGenericDataType
from api.messages.intent_recognition.intent_data_type.cosine_similarity_data import CosineSimilarityData
from api.messages.intent_recognition.intent_data_type.cosine_similarity_response import CosineSimilarityResponse
from api.messages.response_formatter import ResponseFormatter


class ResponsesGenerator(ProxyInterface):
    """Original responses generator service that is responsible for searching a response based on the user's intent."""

    def handle_request(self, user_request: Request) -> Response:
        """
        Manage messages submitted by users.

        :param user_request: The request submitted by the user.
        :return: The response generated by the chatbot.
        """

        # Get user message from user request
        raw_data = [user_request.get_json()['user_message']]

        # Create a group of data builders
        syntax_cleaner: DataBuilder = SyntaxCleaner()
        stop_words_cleaner: DataBuilder = StopWordsCleaner()
        lemmatizer: DataBuilder = Lemmatizer()

        # Set the order of the data builds
        syntax_cleaner.set_next_builder(stop_words_cleaner)
        stop_words_cleaner.set_next_builder(lemmatizer)

        # Get built user message
        user_message_built = syntax_cleaner.build_data(raw_data).pop()

        # Get documents from a database
        from static.documents import documents
        documents: list[dict] = documents.documents

        # Create an intent recognizer factory
        intent_recognizer_factory: IntentRecognizerFactory = CosineSimilarityFactory()

        # Iterate each document to process the user intent with its training data
        for document in documents:
            # Clean the data of the current document
            document_utterances = syntax_cleaner.build_data(document['utterances'])

            intent_data: IntentGenericDataType = CosineSimilarityData(user_message_built, document_utterances)
            intent_result: CosineSimilarityResponse = intent_recognizer_factory.process_user_intent(intent_data)

            # Give a response based on the recognized intent
            if intent_result.recognition_status:
                return ResponseFormatter.get_recognized_response(document)

        # Give a no recognized intent
        return ResponseFormatter.get_no_recognized_response()