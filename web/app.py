import os
from flask import Flask, render_template, session, redirect, url_for, flash
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SECRET_KEY"] = 'minmhan'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
manager = Manager(app)
bootstrap = Bootstrap(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')
    
    def __repr__(self):
        return '<Role %r>' % self.name
        
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))    
    
    def __repr__(self):
        return '<User %r>' % self.username
    

@app.route('/', methods=['GET','POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        old_name = session.get('title')
        if old_name is not None and old_name != form.title.data:
            flash('Look like you have changed your title!')
        session['title'] = form.title.data
        form.title.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, title=session.get('title'))


@app.route('/user/<name>')    
def user(name):
    return '<h1>hello %s</h1>' % name


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


class SearchForm(Form):
    title = StringField('Book Title?', validators=[Required()])
    submit = SubmitField('Submit')


if __name__ == '__main__':
    #app.run(debug=True)
    manager.run()