from datetime import datetime

from flask import Response, jsonify, render_template


class ResponseFormatter:
    """Creates the object that will be sent as a response to the user."""

    @staticmethod
    def get_recognized_response(document: dict) -> Response:
        """
        Create the response object from the information in a document.

        :param document: The document related with the response.
        :return: A response object that will be sent to the user.
        """

        chatbot_response = {
            'time': f'{datetime.now().hour}:{datetime.now().minute}',
            'chatbot_messages': []
        }
        responses = document['responses']

        for response in responses:
            if response['type'] == 'text':
                chatbot_response['chatbot_messages'].append(
                    render_template('messages/text_message.html', data=response)
                )
            elif response['type'] == 'link':
                chatbot_response['chatbot_messages'].append(
                    render_template('messages/link_message.html', data=response)
                )
            elif response['type'] == 'image':
                chatbot_response['chatbot_messages'].append(
                    render_template('messages/image_message.html', data=response)
                )

        return jsonify(chatbot_response)

    @staticmethod
    def get_no_recognized_response() -> Response:
        """
        Creates the response object for a message that has not been acknowledged.

        :return: A response object that will be sent to the user.
        """

        error = {'error_message': 'No puedo entender tu mensaje. Prueba a escribirlo de otra forma.'}
        return jsonify({'error': render_template('error/no_recognized_message.html', data=error)})
