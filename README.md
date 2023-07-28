# FIS Chatbot API

A **rules-based chatbot** API that answers frequently asked questions from FIS students.

## Content
[1. Description](#1-description)  
[2. Requirements](#2-requirements)  
[3. Fixes](#3-fixes)

## 1. Description

The API is responsible for receiving messages to generate various types of responses, such as text, images, links, 
actions and forms. The API currently uses calculations supported by **Cosine Similarity** to identify user intent.
Then, the intent is associated with a given response and is sent to the user.

## 2. Requirements

To ensure the correct operation of the project, it is necessary to have the appropriate versions of 
the tools shown below:

* Python 3.11.4
* Flask 2.3.2
* Flask-Cors 4.0.0
* Jinja2 3.1.2
* Gunicorn 21.2.0
* PyCharm 2023.1.4
* Unidecode 1.3.6
* NLTK 3.8.1
* spaCy 3.6.0
* scikit-learn 1.3.0

## 3. Fixes

After installing all the dependencies specified in the ``Requirements.txt`` file, 
it is necessary to execute the following command from the system terminal 
to install the ``es_core_news_sm`` dependency manually:

``python -m spacy download en_core_news_sm``