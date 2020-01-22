from setuptools import setup, find_packages


setup(
    name='sanic-router',
    version='0.1.4',
    packages=find_packages(exclude=('tests/*',)),
    install_requires=('Sanic>=0.7',),
    author='RafRaf',
    author_email='smartrafraf@gmail.com',
    description='Powerful Django-like router for Sanic',
    license='MIT',
    keywords=('sanic', 'router', 'urls'),
    test_suite='tests',
    url='https://github.com/RafRaf/sanic-router',
)
