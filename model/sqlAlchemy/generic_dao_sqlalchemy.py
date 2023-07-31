from utils.db import db
from model.dao.generic_dao import GenericDAO


class GenericDAOSQLAlchemy(GenericDAO):
    def __init__(self, connection_string):
        engine = db.create_engine(connection_string)
        db.Base.metadata.create_all(engine)
        session = db.sessionmaker(bind=engine)
        self.session = session()

    def create(self, entity):
        self.session.add(entity)
        self.session.commit()

    def read(self, id):
        pass

    def update(self, entity):
        self.session.merge(entity)
        self.session.commit()

    def delete(self, entity):
        self.session.delete(entity)
        self.session.commit()
