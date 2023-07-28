from flask import Request, Response, jsonify, render_template

from api.proxy.proxy_interface import ProxyInterface
from api.messages.responses_generator import ResponsesGenerator


class MessagesProxy(ProxyInterface):
    """Implementation of the interface that is used as a generic entry point to the messages services."""

    def __init__(self, responses_generator: ResponsesGenerator):
        """
        Constructor.

        :param responses_generator: The responses generator service to which successful requests are redirected.
        """
        self._responses_generator: ResponsesGenerator = responses_generator

    @staticmethod
    def _validate_data(json_user_data) -> [bool, dict]:
        """
        Validate the data sent in the user message.

        :param json_user_data: The JSON object sent in the user message.
        :return: A boolean value that indicates if the JSON object is valid and
        a dictionary with the HTML of an identify error.
        """
        expected_key = 'user_message'
        max_value_length = 200

        # Check if a valid JSON was sent
        if not json_user_data or expected_key not in json_user_data or len(json_user_data) > 1:
            error = {'error_message': 'Los tipos de datos enviados son inválidos.'}
            return [False, {'error': render_template('error/invalid_message_data.html', data=error)}]

        # Get the value of the key
        value = json_user_data[expected_key]

        # Check the maximum length of the value
        if len(str(value)) > max_value_length:
            error = {
                'error_message': f'La longitud del mensaje excede el límite permitido ({max_value_length} caracteres).'
            }
            return [False, {'error': render_template('error/invalid_message_data.html', data=error)}]

        return [True, {}]

    def handle_request(self, user_request: Request) -> Response:
        json_user_data = user_request.get_json()
        validation_result = self._validate_data(json_user_data)

        if not validation_result[0]:
            return jsonify(validation_result[1])

        return self._responses_generator.handle_request(user_request)
