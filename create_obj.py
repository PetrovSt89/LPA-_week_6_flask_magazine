from webapp import create_app
from webapp.create_obj import create_grades, create_student, create_subject, create_course

app = create_app()
with app.app_context():
    # create_course.hand_create_course()
    # create_subject.hand_create_subject()
    create_student.hand_create_student()