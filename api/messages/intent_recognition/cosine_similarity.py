from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from api.messages.intent_recognition.intent_recognizer import IntentRecognizer
from api.messages.intent_recognition.intent_data_type.cosine_similarity_data import CosineSimilarityData
from api.messages.intent_recognition.intent_data_type.cosine_similarity_response import CosineSimilarityResponse


class CosineSimilarity(IntentRecognizer):
    """Concrete intent recognizer that uses a cosine similarity process to recognize the user intent."""

    SIMILARITY_BREAKPOINT = 0.7

    def get_user_intent(self, intent_data: CosineSimilarityData) -> CosineSimilarityResponse:
        """
        Determine the user intent based on the user's message and the existing set of phrases.

        :param intent_data: Object with the data needed for the intent recognizer to get the user intent.
        :return:
        """

        # Create the TF-IDF vectorizer
        vectorizer = TfidfVectorizer()

        # Build the TF-IDF array
        tfidf_matrix = vectorizer.fit_transform([intent_data.user_message] + intent_data.training_data)

        # Calcular la similitud del coseno entre las frases
        similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

        # Iterate each similarity value of the similarity matrix to compare it with the similarity breakpoint
        max_similarity_value = similarity_matrix[0][1]

        for similarity_value in similarity_matrix[0][1:]:
            if similarity_value > max_similarity_value:
                max_similarity_value = similarity_value

        response = CosineSimilarityResponse(
            True if max_similarity_value >= self.SIMILARITY_BREAKPOINT else False,
            max_similarity_value
        )

        return response
