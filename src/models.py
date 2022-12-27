import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'principal_user'
    # Here we define columns for the table principal_user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone = Column(Integer, nullable=False)
    password = Column(String(250), nullable=False)
    registration_date = Column(String(250), nullable=False)

class Character_Game_of_Thrones(Base):
    __tablename__ = 'characters_got'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250))
    last_name = Column(String(250))

class FAV_Character_Game_of_Thrones(Base):
    __tablename__ = 'fav_characters_got'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250))
    last_name = Column(String(250))
    principal_user_id = Column(Integer, ForeignKey('principal_user.id'))
    character_got_id = Column(Integer, ForeignKey('characters_got.id'))
    relationship_characters = relationship ('Character_Game_of_Thrones')
    relationship_user = relationship ('principal_user')

class House_Game_of_Thrones(Base):
    __tablename__ = 'houses_got'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250))
    last_name = Column(String(250))

class FAV_House_Game_of_Thrones(Base):
    __tablename__ = 'fav_houses_got'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250))
    last_name = Column(String(250))
    principal_user_id = Column(Integer, ForeignKey('principal_user.id'))
    houses_got_id = Column(Integer, ForeignKey('houses_got.id'))
    relationship_houses = relationship ('houses_got')
    relationship_user = relationship ('principal_user')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
