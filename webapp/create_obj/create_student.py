
from webapp.db import db

from webapp.magazine.models import Student


def save_student(student_name, student_surname, course_id, subj_id):
    stud = Student(student_name=student_name, student_surname=student_surname,
                        course_id=course_id, subj_id=subj_id)
    db.session.add(stud)
    db.session.commit()


def hand_create_student():

    student_name = 'Масяня'
    student_surname ='Белопузов'
    course_id = 3
    subj_id = 2
    save_student(student_name=student_name, student_surname=student_surname,
                    course_id=course_id, subj_id=subj_id)


