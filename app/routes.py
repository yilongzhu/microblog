from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Yilong'}
    posts = [
            {'author': {'username': 'Daniel'},
             'body': 'Wow, I can\'t believe I skipped gymnastics to dance.'},
            {'author': {'username': 'Sam'},
             'body': 'It must be weird to go from taking a Lyft to Target to going to class.'}
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)