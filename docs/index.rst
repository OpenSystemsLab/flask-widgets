.. flask-widgets documentation master file, created by
   sphinx-quickstart on Fri May  9 22:40:54 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Flask-Widgets
=============

This extension provides basic template widget feature for `Flask <http://flask.pocoo.org>`_

.. module:: flask.ext.widgets

Installing Flask-Widgets
------------------------

Install with **pip**::

    pip install flask-widgets

Set Up
------
Widgets is managed through a ``Widgets`` instance::

    from flask import Flask
    from flask.ext.widgets import Widgets

    app = Flask(__name__)

    widgets = Widgets(app)

You may also set up your ``Widgets`` instance later at configuration time using
**init_app** method::

    widgets = Widgets()

    app = Flask(__name__)
    widgets.init_app(app)

Register Widgets
----------------

To register a single widget or a group of them, you will use the :meth:`~Widgets.widget` and  :meth:`~Widgets.position` decorators::

    @widgets.widget('title')
    def title():
        return 'Flask-Widget example'

    @widgets.position('sidebar', order=1)
    def sidebar_featured_items():
        return dict(the='variables', go='here')

The example above will register a standalone widget named ``title`` and position ``sidebar``

To reorder the widgets in a position, adjust the ``order`` variable, widget with less order will render first

Widget method must return a `dict` of variables or a string, in case it returns a `dict`,
``Widgets`` with render them with a template has same name as the method ``widgets/sidebar_featured_items.html``
You can register as many positions and the number of widgets for them as you want.

Render Widgets in Template:
---------------------------

You will use template methods :meth`widget` and :meth`widgets` to render widgets::

    <!DOCTYPE html>
    <html>
        <head>
            <title>{{ widget('title') }}</title>
        </head>
        <body>
            <div style="border:1px solid #ccc">
                {{ widgets('header') }}
            </div>
            Template body
            <div style="border:1px solid #ddd">
                {{ widgets('footer') }}
            </div>
        </body>
    </html>


``Widgets`` will render registered widgets for you, if you need

Notes:
------

* The extension is in development, use it ask your own risk
* If you have better ideas or any suggestion please feel free to contact me
* If you can improve this document, please help!


