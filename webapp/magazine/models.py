import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from webapp.db import db


class News(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    url = Column(String, unique=True, nullable=True) 
    published = Column(DateTime(timezone=True), nullable=False)
    text = Column(Text, nullable=True)
    # comments = relationship('Comment', backref='news')
    # comments: Mapped[List["News"]] = relationship(back_populates="news")

    def comments_count(self):
        return Comment.query.filter(Comment.news_id == self.id).count()       

    def __repr__(self) -> str:
        return f"<News {self.title} {self.url}>"
    

class Comment(db.Model):
    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    created = Column(
        DateTime(timezone=True), nullable=False, default=datetime.datetime.now()
        )
    news_id = Column(Integer, ForeignKey('news.id', ondelete="CASCADE"), index=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete="CASCADE"), index=True)
    subj_id = Column(Integer, ForeignKey('subj.id', ondelete="CASCADE"), index=True)
    news = relationship('News', backref='comments')
    user = relationship('User', backref='comments')
    subj = relationship('Subj', backref='comments')


    def __repr__(self) -> str:
        return f"<Comment {self.id}>"
    

class Course(db.Model):
    id = Column(Integer,primary_key=True)
    course_name = Column(String, nullable=False)
    # subj_id = Column(Integer, ForeignKey('subj.id', ondelete="CASCADE"), index=True)
    # student_id = Column(Integer, ForeignKey('student.id', ondelete="CASCADE"), index=True)

class Student(db.Model):
    id = Column(Integer,primary_key=True)
    student_name = Column(String, nullable=False)
    student_surname = Column(String, nullable=False)
    course_id = Column(Integer, ForeignKey('course.id', ondelete="CASCADE"), index=True)
    # grade_id = Column(Integer, ForeignKey('grade.id', ondelete="CASCADE"), index=True)
    subj_id = Column(Integer, ForeignKey('subj.id', ondelete="CASCADE"), index=True)


class Subj(db.Model):
    id = Column(Integer,primary_key=True)
    subject = Column(String)
    # course_id = Column(Integer, ForeignKey('course.id', ondelete="CASCADE"), index=True)
    # student_id = Column(Integer, ForeignKey('student.id', ondelete="CASCADE"), index=True)


class Grade(db.Model):
    id = Column(Integer,primary_key=True)
    grades_name = Column(String, nullable=False)
    student_id = Column(Integer, ForeignKey('student.id', ondelete="CASCADE"), index=True)
    subj_id = Column(Integer, ForeignKey('subj.id', ondelete="CASCADE"), index=True)
    # student = relationship('Student', backref='grade')


# class StudentSubject(db.Model):
#     student_id = Column(Integer, ForeignKey('student.id', ondelete="CASCADE"), index=True)
#     subj_id = Column(Integer, ForeignKey('subj.id', ondelete="CASCADE"), index=True)