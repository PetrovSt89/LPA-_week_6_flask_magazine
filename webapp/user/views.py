from flask import Blueprint, render_template, flash, redirect, url_for
from webapp.user.models import User
from webapp.user.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user
from webapp.db import db


blueprint = Blueprint(name='user', import_name=__name__, url_prefix='/users')

@blueprint.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect(location=url_for(endpoint='magazine.index'))
    page_title = 'Авторизация'
    login_form = LoginForm()
    return render_template('user/login.html',
                        page_title=page_title, login_form=login_form)


@blueprint.route("/process-login", methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user=user, remember=form.remember_me.data)
            flash('Вы успешно вошли на сайт')
            return redirect(location=url_for(endpoint='magazine.index'))
    flash('Неправильное имя или пароль')
    return redirect(location=url_for(endpoint='user.login'))


@blueprint.route("/logout")
def logout():
    logout_user()
    flash('Вы успешно разлогинились')
    return redirect(location=url_for(endpoint='magazine.index'))


@blueprint.route("/register")
def register():
    if current_user.is_authenticated:
        return redirect(location=url_for(endpoint='magazine.index'))
    page_title = 'Регистрация'
    reg_form = RegistrationForm()
    return render_template('user/registration.html',
                        page_title=page_title, reg_form=reg_form)


@blueprint.route("/process-reg", methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались')
        return redirect(location=url_for(endpoint='user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(
                    getattr(form, field).label.text,error
                    ))
        return redirect(location=url_for(endpoint='user.register'))


@blueprint.route("/user.home")
def user_home():
    page_title = f'Домашняя страница'
    text_message = f'Привет {current_user.username}'

    return render_template('admin/admin.html',
                    page_title=page_title, text_message=text_message)