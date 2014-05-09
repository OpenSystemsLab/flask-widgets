from flask import Flask, render_template
from flask_widgets import Widgets
app = Flask(__name__)

app.config.update({
    'DEBUG': True
})

widgets = Widgets(app)

@widgets.widget('title')
def title():
    return 'Flask-Widget example'

@widgets.widget('say')
def say(msg):
    return 'says %s!' % msg


@widgets.position('header', order=100)
def hello_world():
    return {'greeting': 'HELLO WORLD'}


@widgets.position('header')
def welcome():
    return '<h1>Welcome to Flask-Widgets</h1>'

@widgets.position('footer')
def welcome():
    return 'Flask-Widgets by Bruce Doan'


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
