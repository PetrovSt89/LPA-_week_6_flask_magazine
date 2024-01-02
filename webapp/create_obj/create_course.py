
from webapp.db import db

from webapp.magazine.models import Course


def save_course(course_name):
    course = Course(course_name=course_name)
    db.session.add(course)
    db.session.commit()


def hand_create_course():
    for i in ['7', '8', '9', '10']:
        course_name = i
        save_course(course_name=course_name)




