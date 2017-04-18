# -*- coding: utf-8 -*-

"""Flask & ReactJS."""

from setuptools import find_packages, setup

readme = 'Flask & ReactJS Boilerplate'
# open('README.rst').read()

install_requires = [
    "Flask-Security-fork",
    "Flask-SQLAlchemy",
    "Flask",
    "bcrypt",
]

setup_requires = [
    'pytest-runner>=2.6.2',
]

tests_require = [
    'Flask-CLI>=0.4.0',
    'bcrypt>=1.0.2',
    'check-manifest>=0.25',
    'coverage>=4.0',
    'isort>=4.2.2',
    'mock>=1.0.1',
    'pony>=0.7.1',
    'pydocstyle>=1.0.0',
    'pytest-cache>=1.0',
    'pytest-cov>=2.4.0',
    'pytest-flakes>=1.0.1',
    'pytest-flask>=0.10.0',
    'pytest-pep8>=1.0.6',
    'pytest>=3.0.5',
    'Flask-SQLAlchemy>=2.2',
    'py>=1.4.26'
]

setup(
    name='flask-reactjs',
    version='1',
    description=__doc__,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    long_description=readme,
    keywords='flask, react, sqlalchemy, flask-security',
    license='GPLv3',
    author='Aldo María Vizcaino',
    author_email='aldo.vizcaino87@gmail.com',
    setup_requires=setup_requires,
    tests_require=tests_require,
    install_requires=install_requires,
)
