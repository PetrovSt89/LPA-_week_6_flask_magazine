from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from webapp.db import db


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String, index=True, unique=True)
    password = Column(String) 
    role = Column(Text, index=True)
    email = Column(String, nullable=True)


    def set_password(self, password):
        self.password = generate_password_hash(password=password)


    def check_password(self, password):
        return check_password_hash(pwhash=self.password, password=password)


    @property
    def is_admin(self):
        return self.role == 'admin'


    def __repr__(self) -> str:
        return f"<User {self.username} {self.id} {self.role}>"
    