from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Eric'} #a mock user object for this app
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Denver!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Revnant was gory'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
