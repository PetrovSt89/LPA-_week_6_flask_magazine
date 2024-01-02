
from webapp.db import db

from webapp.magazine.models import Grade


def save_grade(grade_name, student_id):
    grade = Grade(grades_name=grade_name, student_id=student_id)
    db.session.add(grade)
    db.session.commit()


def hand_create_grade():
    grade_name = '5'
    student_id = 2
    save_grade(grade_name=grade_name, student_id=student_id)
