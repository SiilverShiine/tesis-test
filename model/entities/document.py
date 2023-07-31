from utils.db import db


# TODO: Define the string size
class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    utterances = db.relationship("Utterance", back_populates="document")
    responses = db.relationship("Response", back_populates="document")
