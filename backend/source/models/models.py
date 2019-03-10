# -*- coding: utf-8 -*-
from core.database import Base
from sqlalchemy import Column, Integer, String


class Entry(Base):
    """
    Entry table
    """
    __tablename__ = "entry"
    id = Column(Integer, primary_key=True, nullable=False)
    value = Column(String(256), nullable=False)
    date = Column(String(128), nullable=False)

    def __str__(self):
        return f"{self.id}, {self.value}, {self.date}"
