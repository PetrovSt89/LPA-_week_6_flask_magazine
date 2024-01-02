from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError

from webapp.magazine.models import News, Subj


class CommentForm(FlaskForm):
    subj_id = HiddenField('ID предмета', validators=[DataRequired()])
    comment_text = StringField('Ваш комментарий', validators=[DataRequired()])
    submit = SubmitField('Отправить')


    def validate_news_id(self, news_id):
        if not News.query.get(news_id.data):
            raise ValidationError('Новости с таким id не существует')
        

    def validate_subj_id(self, subj_id):
        if not Subj.query.get(subj_id.data):
            raise ValidationError('Предмета с таким id не существует')
        

class SelectionForm(FlaskForm):
    course = StringField('Введите класс')
    subj = StringField('Введите предмет')
    submit = SubmitField('Отправить')


class GradeForm(FlaskForm):
    student_id = IntegerField('Введите ID ученика', validators=[DataRequired()])
    subj = StringField('Введите предмет', validators=[DataRequired()])
    grade_name = StringField('Введите оценку', validators=[DataRequired()])
    submit = SubmitField('Отправить')


class SubjForm(FlaskForm):
    subj = StringField('Введите название предмета', validators=[DataRequired()])
    submit = SubmitField('Отправить')


class CourseForm(FlaskForm):
    course = StringField('Введите название класса', validators=[DataRequired()])
    submit = SubmitField('Отправить')