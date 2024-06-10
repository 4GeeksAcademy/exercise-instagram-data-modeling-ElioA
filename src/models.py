import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email       
        }
    
class Follower(Base):
    __tablename__ = 'follower'
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def __repr__(self):
        return f'<follower {self.user_from_id}>'
    
    def serialize(self):
        return {
            "user_to_id": self.user_to_id,
            "user_from_id": self.user_from_id     
        }

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def __repr__(self):
        return f'<Post {self.id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self. user_id       
        }
    
class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

    def __repr__(self):
        return f'<Media {self.id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "url": self.url,
            "post_id": self.post_id       
        }

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    text = Column(String(500))
    author_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    

    def __repr__(self):
        return f'<Comment {self.id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "text": self.text,
            "author_id": self.author_id,
            "post_id": self.post_id
        }
    




## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
