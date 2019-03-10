# -*- coding: utf-8 -*-
import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from utils import construct_db_uri

logger = logging.getLogger(__name__)

db_uri = construct_db_uri(
    {
        "user": "postgres",
        "password": "",
        "host": "postgres",
        "port": "5432",
        "database": "api_db"
    }
)
db_user = ""
engine = create_engine(db_uri, convert_unicode=True)
# Use autocommit because 'get_entry' was in "idle on transaction" forever
session = scoped_session(sessionmaker(autocommit=True,
                                      autoflush=True,
                                      bind=engine))

Base = declarative_base()
Base.query = session.query_property()
metadata = Base.metadata


def init_db():
    import models.models
    Base.metadata.create_all(engine, checkfirst=True)


def add_entry(entry):
    id = None
    session.begin()
    try:
        session.add(entry)
        session.flush()
        id = entry.id
        session.commit()
    except:
        session.rollback()

    return id


def get_all_entries():
    from models.models import Entry

    entries = None
    session.begin()
    try:
        entries = session.query(Entry) \
            .all()
        session.commit()
    except:
        session.rollback()

    return entries


def get_entry(entry_id):
    from models.models import Entry

    entry = None
    session.begin()
    try:
        entry = session.query(Entry) \
            .filter_by(id=entry_id) \
            .all()
        session.commit()
    except:
        session.rollback()

    return entry


def update_entry(entry_id, entry):
    from models.models import Entry

    session.begin()
    try:
        session.query(Entry) \
            .filter_by(id=entry_id) \
            .update(entry)
        session.commit()
    except:
        session.rollback()

    return entry_id


def delete_entry(entry_id):
    from models.models import Entry

    session.begin()
    try:
        session.query(Entry) \
            .filter_by(id=entry_id) \
            .delete()
        session.commit()
    except:
        session.rollback()

    return entry_id


def close():
    session.close()
    engine.dispose()
