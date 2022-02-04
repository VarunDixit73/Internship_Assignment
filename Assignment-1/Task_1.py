from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'Repository'
    PhoneNo = Column(Integer,primary_key=True) 
    User_Name = Column(String(20))
    Age = Column(Integer)
    Gender = Column(String(10))
    def __str__(self) -> str:
        return f'{self.User_Name} {self.Age} {self.Gender}'

class Upload(Base):
    __tablename__ = 'Contact'
    PhoneNo = Column(Integer,primary_key=True) 
    CName = Column(String(20))
    CNumb = Column(Integer)
    def __str__(self) -> str:
        return f'{self.PhoneNo} {self.CName} {self.CNumb}'


class ChatView(Base):
    __tablename__ = 'Chats'
    PhoneNo = Column(Integer,primary_key=True)
    chat = Column(String) 
    def __str__(self) -> str:
        return f'{self.chat}'

def open_db():
    engine = create_engine('sqlite:///review.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

open_db()