from model.sqlAlchemy.generic_dao_sqlalchemy import GenericDAOSQLAlchemy
from model.entities.document import Document
from model.dao.document_dao import DocumentDAO


class DocumentDaoSqlAlchemy(GenericDAOSQLAlchemy[Document], DocumentDAO):
    def __init__(self, connection_string):
        super().__init__(connection_string)

    def get_documents_by_something(self, something):
        return self.session.query(Document).filter_by(title=something).all()
