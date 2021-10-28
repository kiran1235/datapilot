from server import db
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.sql.sqltypes import DateTime

class Configuration(db.Model):
    __tablename__ = "config"
    id = Column(Integer, primary_key=True)
    key = Column(String(32))
    value = Column(String(2000))
    isdeleted = Column(Boolean)
    created_on = Column(TIMESTAMP)
    updated_on = Column(TIMESTAMP)

class Dictionary(db.Model):
    __tablename__ = "dictionary"
    id = Column(Integer, primary_key=True)
    key = Column(String(32))
    value = Column(String(2000))
    isdeleted = Column(Boolean)
    created_on = Column(TIMESTAMP)
    updated_on = Column(TIMESTAMP)

class Migratons(db.Model):
    __tablename__ = "migration"
    id = Column(Integer, primary_key=True)
    key = Column(String(32))
    value = Column(String(2000))
    isdeleted = Column(Boolean)
    created_on = Column(TIMESTAMP)
    updated_on = Column(TIMESTAMP)
