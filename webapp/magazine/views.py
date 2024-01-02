from webapp.config import city
from flask import abort, Blueprint, render_template, flash, redirect, request, url_for
from flask_login import current_user, login_required
from webapp.magazine.models import Comment, News
from webapp.magazine.forms import CommentForm, SelectionForm, GradeForm, SubjForm, CourseForm

from webapp.magazine.models import Course, Student, Subj, Grade
from dataclasses import dataclass

from webapp.db import db



blueprint = Blueprint(name='magazine', import_name=__name__)


@dataclass
class Magazine:
    course: Course|None = None
    student: Student|None = None
    subj: Subj|None = None
    grades: Grade|None = None


@blueprint.route("/")
def index():
    page_title = 'Электронный журнал'
    magazine = Magazine(course=Course.query.all(),
                        student=Student.query.all(),
                        subj=Subj.query.all(),
                        grades=Grade.query.all())
    return render_template('magazine/index.html',
                        page_title=page_title, magazine=magazine)


@blueprint.route("/magazine/subjects")
def subj():
    page_title = f'Предметы'
    subj_form = SubjForm()
    subjects = Subj.query.all()

    return render_template('magazine/subjects.html',
                    page_title=page_title, subjects=subjects, subj_form=subj_form)


@blueprint.route("/magazine/process-subjects/", methods=['POST'])
def process_subjects():
    form = SubjForm()
    subj = Subj(subject=form.subj.data)
    db.session.add(subj)
    db.session.commit()
    flash('Предмет успешно добавлен')
    return redirect(location=url_for(endpoint='magazine.subj'))


@blueprint.route("/magazine/subjects/<int:subj_id>")
def single_subj(subj_id):
    my_subj = Subj.query.filter(Subj.id == subj_id).first()
    if not my_subj:
        abort(404)
    return render_template(
        'magazine/single_subj.html', page_title=my_subj.subject, 
        subj=my_subj
        )


@blueprint.route("/magazine/stud")
def stud():
    page_title = f'Выбор по классу и предмету'
    sel_form = SelectionForm()
    grade_form = GradeForm()
    return render_template('magazine/stud.html',
                    page_title=page_title, sel_form=sel_form)


@blueprint.route("/magazine/process-stud/", methods=['POST'])
def process_stud():
    sel_form = SelectionForm()
    course = Course.query.filter(Course.course_name == sel_form.course.data).first()
    subject = Subj.query.filter(Subj.subject == sel_form.subj.data).first()
    if not subject and not course:
        stud = Student.query.all()
        subject = Subj.query.all()
        course = Course.query.all()
    elif not subject:
        stud = Student.query.filter(Student.course_id == course.id).all()
        subject = Subj.query.all()
        course = [course]
    elif not course:
        stud = Student.query.filter(Student.subj_id == subject.id).all()
        course = Course.query.all()
        subject = [subject]
    else:
        stud = Student.query.filter(Student.course_id == course.id).filter(Student.subj_id == subject.id).all()
        subject = [subject]
        course = [course]
    grades = Grade.query.all()
    grade_form = GradeForm()
    if not stud or not course:
        abort(404)
    return render_template(
        'magazine/stud.html', page_title='Выборка',
        course = course, subject=subject, stud=stud, grades=grades, grade_form=grade_form, sel_form=sel_form)


@blueprint.route("/magazine/process-grade/", methods=['POST'])
def process_grade():
    form = GradeForm()
    subj = Subj.query.filter(Subj.subject == form.subj.data).first()
    student = Student.query.filter(Student.id == form.student_id.data).first()
    if not subj or not student:
        abort(404)
    grade = Grade(
            grades_name=form.grade_name.data, student_id=student.id , subj_id=subj.id
            )
    db.session.add(grade)
    db.session.commit()
    flash('оценка успешно добавлена')
    return redirect(location=url_for(endpoint='magazine.stud'))



@blueprint.route("/magazine/courses")
def course():
    page_title = f'Классы'
    courses = Course.query.all()
    course_form = CourseForm()
    return render_template('magazine/courses.html',
                    page_title=page_title, course_form=course_form, courses=courses)


@blueprint.route("/magazine/process-course/", methods=['POST'])
def process_course():
    form = CourseForm()
    course = Course(course_name=form.course.data)
    db.session.add(course)
    db.session.commit()
    flash('Класс успешно добавлен')
    return redirect(location=url_for(endpoint='magazine.course'))


@blueprint.route("/magazine/courses/<int:course_id>")
def single_course(course_id):
    my_course = Course.query.filter(Course.id == course_id).first()
    if not my_course:
        abort(404)
    return render_template(
        'magazine/single_course.html', page_title=my_course.course_name, 
        course=my_course
        )


@blueprint.route("/news/comment", methods=['POST'])
@login_required
def add_comment():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(
            text=form.comment_text.data, news_id=form.news_id.data, user_id=current_user.id
            )
        db.session.add(comment)
        db.session.commit()
        flash('Комментарий успешно добавлен')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(
                    getattr(form, field).label.text,error
                    ))
    return redirect(request.referrer)
