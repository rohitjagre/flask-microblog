from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Rohit'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Blog-1'
        },
        {
            'author': {'username': 'Mary'},
            'body': 'Blog-2'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
