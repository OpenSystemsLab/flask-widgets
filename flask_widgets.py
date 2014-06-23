__version__ = '0.4'
__versionfull__ = __version__


from flask import current_app, Markup, render_template, request

def _make_cache_key(key_prefix):
    """Make cache key from prefix
    Borrowed from Flask-Cache extension
    """
    if callable(key_prefix):
        cache_key = key_prefix()
    elif '%s' in key_prefix:
        cache_key = key_prefix % request.path
    else:
        cache_key = key_prefix

    cache_key = cache_key.encode('utf-8')

    return cache_key


class Widgets():
    _positions = dict()
    _widgets = dict()
    _cache = 'a'

    def __init__(self, app=None, cache=None):

        self.app = app
        if app is not None:
            self.init_app(app, cache)

    def init_app(self, app, cache):
        app.widgets = self
        self._cache = cache

        app.jinja_env.globals['widgets'] = self.render_widget_position
        app.jinja_env.globals['widget'] = self.render_widget

    def render_widget_position(self, position, **options):
        if position not in self._positions:
            current_app.logger.warning('Position not found: %s' % position)
            return ''

        cache_timeout = options.pop('timeout', None)
        cache_key = _make_cache_key(options.pop('key_prefix', 'widgets-%s' % position))

        if self._cache and cache_timeout:
            output = self._cache.get(cache_key)
            if output:
                return output

        output = ''
        widgets = self._positions[position]
        for widget in widgets:
            f = widget[0]
            res = f()
            if res is None:
                return ''
            if not isinstance(res, basestring):
                template = 'widgets/%s.html' % f.__name__
                output += Markup(render_template(template, **res))
            else:
                output += Markup(res)

        if self._cache and cache_timeout:
            self._cache.set(cache_key, output, timeout=cache_timeout)
        return output

    def render_widget(self, name, **options):
        if name in self._widgets:
            cache_timeout = options.pop('timeout', None)
            cache_key = _make_cache_key(options.pop('key_prefix', 'widget_%s' % name))

            if self._cache and cache_timeout:
                output = self._cache.get(cache_key)
                if output:
                    return output

            f = self._widgets[name]
            res = f(**options)
            if res is None:
                return ''
            if not isinstance(res, basestring):
                template = 'widgets/%s.html' % f.__name__
                output = Markup(render_template(template, **res))
            else:
                output = Markup(res)

            if self._cache and cache_timeout:
                self._cache.set(cache_key, output, timeout=cache_timeout)

            return output

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




