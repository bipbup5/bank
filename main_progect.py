import datetime
import os

from flask_login import login_user, LoginManager, login_required, logout_user

from data import db_session
from flask import Flask, render_template, request, make_response, session, jsonify
from flask_restful import Api
from werkzeug.utils import redirect

from data.staff import Staff
from forms.loginform import LoginForm
from forms.registerform import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная страница')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(Staff).filter(Staff.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@login_manager.user_loader
def load_user(id):
    db_sess = db_session.create_session()
    return db_sess.query(Staff).get(id)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(Staff).filter(Staff.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        staff = Staff(
            nickname=form.nickname.data,
            email=form.email.data,
        )
        staff.set_password(form.password.data)
        db_sess.add(staff)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


def main():
    db_session.global_init("db/bank.db")
    app.run(port=8000, host='localhost')


if __name__ == '__main__':
    main()
