__version__ = '0.1'
__versionfull__ = __version__


from flask import current_app, Markup, render_template


class Widgets():
    _positions = dict()
    _widgets = dict()

    def __init__(self, app=None):

        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.widgets = self

        app.jinja_env.globals['widgets'] = self.render_widget_position
        app.jinja_env.globals['widget'] = self.render_widget

    @classmethod
    def render_widget_position(self, position):
        if position not in self._positions:
            current_app.logger.warning('Position not found: %s' % position)
            return ''

        output = ''
        widgets = self._positions[position]
        for widget in widgets:
            f = widget[0]
            res = f()
            if not isinstance(res, basestring):
                template = 'widgets/%s.html' % f.__name__
                output += Markup(render_template(template, **res))
            else:
                output += Markup(res)
        return output

    @classmethod
    def render_widget(self, name, *options):
        if name in self._widgets:
            f = self._widgets[name]
            res = f(*options)
            if not isinstance(res, basestring):
                template = 'widgets/%s.html' % f.__name__
                return Markup(render_template(template, **res))
            else:
                return Markup(res)
        return ''

    @property
    def widgets(self):
        app = self.app or current_app
        return app.widgets

    def widget(self, name):
        def decorator(f):
            self._widgets[name] = f
        return decorator

    def position(self, position, order=None):
        if order is None:
            order = -1

        def decorator(f):
            if position not in self._positions:
                self._positions[position] = list()
            self._positions[position].append((f, order))

            self._positions[position] = sorted(self._positions[position], key=lambda k: k[1])
        return decorator




