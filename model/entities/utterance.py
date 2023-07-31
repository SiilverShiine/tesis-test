from utils.db import db


# TODO: Define the string size
class Utterance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100))
    document = db.relationship("Document", back_populates="utterances")
