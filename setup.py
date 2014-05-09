"""
Flask-Widgets
-------------

Basic widgets support for Flask
"""
from setuptools import setup

setup(
    name='Flask-Widgets',
    version='0.1',
    url='https://github.com/rgv151/flask-widgets',
    license='MIT',
    author='Bruce Doan',
    author_email='me@huy.im',
    description='Basic widgets support for Flask',
    long_description=__doc__,
    py_modules=['flask_widgets'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Flask',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)