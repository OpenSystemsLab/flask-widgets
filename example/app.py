from flask import Flask, render_template
from flask.ext.widgets import Widgets
from flask.ext.cache import Cache
from datetime import datetime

app = Flask(__name__)

app.config.update({
    'DEBUG': True,
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': 'redis://localhost:6379/2'
})

cache = Cache(app)
widgets = Widgets(app, cache=cache)


@widgets.widget('title')
def title():
    return 'Flask-Widget example'

@widgets.widget('say')
def say(msg):
    return 'says %s!<br>Last cached time for this widget was: %s' % (msg, datetime.now())


@widgets.position('header', order=100)
def hello_world():
    return {'greeting': 'HELLO WORLD'}


@widgets.position('header')
def welcome():
    return '<h1>Welcome to Flask-Widgets</h1>'

@widgets.position('footer')
def welcome():
    return 'Flask-Widgets by Bruce Doan<br>Last cached time for this widget was: %s' % datetime.now()


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
