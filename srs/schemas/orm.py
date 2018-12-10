from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql.json import JSONB


Base = declarative_base()


class Schema:
    __tablename__ = 'schemas'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement='auto')
    schema = Column(JSONB)


def init_db(uri):
    engine = create_engine(uri, convert_unicode=True, echo=False)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    return db_session
