"""
Flask-Widgets
-------------

Basic widgets support for Flask
"""
from setuptools import setup

setup(
    name='Flask-Widgets',
    version='0.2',
    url='https://github.com/rgv151/flask-widgets',
    license='MIT',
    author='Bruce Doan',
    author_email='me@huy.im',
    description='This extension provides basic template widget feature for Flask',
    long_description=__doc__,
    py_modules=['flask_widgets'],
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
