import nltk
from flask import Flask, Request, request, send_from_directory
from flask_cors import CORS

from api.proxy.proxy_interface import ProxyInterface
from api.proxy.messages_proxy import MessagesProxy
from api.messages.responses_generator import ResponsesGenerator


# Create a Flask application and define CORS policies
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Configure the static route
app.static_folder = 'static'

# Download the set of stop words used to filter the data
nltk.download('stopwords')


@app.route('/')
def default():
    """Provides a response to a request sent to the application root."""

    return 'You shouldn\'t be here!'


@app.route('/images/<image_name>')
def show_image(image_name):
    """Looks for an image in the static folder."""
    return send_from_directory('static/images', image_name)


@app.route('/api/messages', methods=['POST'])
def get_message_response():
    """Looks for a response based on the user's intent and provides an associated response."""
    response_generator: ResponsesGenerator = ResponsesGenerator()
    user_request: Request = request

    return messages_proxy.handle_request(user_request)


if __name__ == '__main__':
    app.run()
