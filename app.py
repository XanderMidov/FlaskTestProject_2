import os
from datetime import datetime
# from zeep_test import get_1S_leftovers
import locale
from flask import Flask, request, make_response, redirect, abort, render_template, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TextAreaField, RadioField, SelectField
from wtforms.validators import DataRequired
from requests import Session
from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from zeep import Client
from zeep.transports import Transport
from datetime import datetime

# def get_1S_leftovers(date):
#     session = Session()
#     session.auth = HTTPBasicAuth('Python', '411209')
#     client = Client('http://localhost/Chezima32/ru_RU/ws/chezima_items.1cws?wsdl',
#         transport=Transport(session=session))
#
#     results = client.service.GetItem(date)
#     return results

# from flask_sqlalchemy import SQLAlchemy
#
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
#
# class NameForm(FlaskForm):
#     name_form = StringField('What is your fucking name?', validators=[DataRequired()])
#     date_form = DateField('Choose date', validators=[DataRequired()])
#     text_form = TextAreaField('Write text')
#     # check1_form
#     select_form = SelectField('Choose your destiny', choices=[('piska', 'Piska'), ('jopa', 'Jopa'), ('siski', 'Siski')])
#     radio_form = RadioField('Choose variant', validators=[DataRequired()], choices=[('jopa', 'Jopa'), ('piska', 'Piska')])
#     submit_form = SubmitField('Submit')
#
# class NewUserForm(FlaskForm):
#     name_form = StringField('Введи имя пользователя', validators=[DataRequired()])
#     select_form = SelectField('Выбери роль', choices=[('User', 'Пользователь'), ('Admin', 'Администратор'), ('Moderator', 'Модератор')])
#     submit_form = SubmitField('Submit')
#
# class LeftoversForm(FlaskForm):
#     date_form = DateField('Получить остатки на дату', validators=[DataRequired()])
#     submit_form = SubmitField('Подтвердить')
#
# basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
# app.config['FLASK_TEST'] = 'SOME FLASK SHIT'
# app.config['SECRET_KEY'] = 'Hard to guess string'
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:786538@localhost:3306/python_flask_2'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
#
# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.INTEGER, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     label = db.Column(db.String(64))
#     user = db.relationship('User', backref='role')
#
#     def __repr__(self):
#         return '<Role %s>' % self.name
#
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), unique=True, index=True)
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
#
#     def __repr__(self):
#         return '<User %s>' % self.username
#
def nav_generate():
    nav_dict = dict()
    for url in app.url_map.iter_rules():
        if url.endpoint != 'static' and url.endpoint != 'user':
            nav_dict.setdefault(url.endpoint.replace('_', ' ').capitalize(), url.rule)
    return nav_dict
#
@app.route('/')
def index():
    nav_dict = nav_generate()
    content = 'Lorem ipsum bla bla bla'
    return render_template('main.html', content_t=content, nav_dict_t=nav_dict)
#
#
# @app.route('/hello_world')
# def hello_world():  # put application's code here
#     nav_dict = nav_generate()
#     content = 'Lorem ipsum bla bla bla'
#     return render_template('main.html', content_t=content, nav_dict_t=nav_dict)
#
#
# def hello_alternate_world():
#     return 'Hello alternate world !!!'
#
# app.add_url_rule('/alt', 'hello_alternate_world', hello_alternate_world)
#
#
# @app.route('/<name>')
# def user(name):
#     nav_dict = nav_generate()
#     content = ''
#     if name == 'alex':
#         content = f'Hello {name}'
#     if name == 'rose':
#         content = f'Hello {name}'
#     if name == 'romashka':
#         content = f'Hello {name}'
#     if name == 'lutik':
#         content = f'Hello {name}'
#     if name == 'georgin':
#         content = f'Hello {name}'
#     if name == 'xander':
#         return redirect('https://www.google.ru/search?q=xander')
#     return render_template('main.html', nav_dict_t=nav_dict, content_t=content)
#
#
# @app.route('/req')
# def request_test():
#     user_agent = request.headers['Sec-Ch-Ua-Platform']
#     return render_template('main.html', content_t=user_agent, nav_dict_t=nav_generate())
#
#
# @app.route('/res_red')
# def response_redirect_test():
#     response = make_response('Shit', 302)
#     response.headers['Location'] = '/lutik'
#     return response
#
# @app.route('/form_work_route', methods=['GET', 'POST'])
# def form_work():
#     content = None
#     form = NameForm()
#     if form.validate_on_submit():
#         session['name'] = form.name_form.data
#         session['radio'] = form.radio_form.data
#         session['date'] = form.date_form.data.strftime('%A-%d-%B-%y')
#         return redirect(url_for('form_work'))
#     content = 'We going to %s and lead to %s at %s' % (session['name'], session['radio'], session['date'])
#     return render_template('form_template.html', nav_dict_t=nav_generate(), form_t=form, content_t=content)
#
# @app.route('/add_new_user_route', methods=['GET', 'POST'])
# def add_new_user():
#     users = None
#     form = NewUserForm()
#     form.select_form.choices = get_roles()
#     if form.validate_on_submit():
#         role = Role.query.filter_by(name=form.select_form.data).first()
#         user = User(username=form.name_form.data, role=role)
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for('add_new_user'))
#     users_and_roles = db.session.query(User.username, Role.name).join(Role).all()
#     users = User.query.all()
#     return render_template('new_user.html', nav_dict_t=nav_generate(), form_t=form, users_t=users_and_roles)
#
# def get_roles():
#     roles = db.session.query(Role.name, Role.label).all()
#     roles_list = list()
#     for role in roles:
#         roles_list.append(tuple(role))
#     return roles_list
#
# @app.route('/leftovers_route', methods=['GET', 'POST'])
# def leftovers():
#     form = LeftoversForm()
#     leftovers = []
#     if form.validate_on_submit():
#         # leftovers = get_1S_leftovers()
#         leftovers = [{'name': 'Jopa', 'count': '4654', 'price': '4654'}]
#         return render_template('leftovers.html', nav_dict_t=nav_generate(), form_t=form, leftovers_t=leftovers)
#     return render_template('leftovers.html', nav_dict_t=nav_generate(), form_t=form, leftovers_t=leftovers)
#

# if __name__ == '__main__':
#     app.run(debug=True)

