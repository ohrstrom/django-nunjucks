from distutils.core import setup

setup(
    name='nunjucks',
    version='0.0.1',
    author='Jonas Ohrstrom',
    author_email='ohrstrom@hazelfire.com',
    packages=['nunjucks',],
    #scripts=[],
    url='https://github.com/ohrstrom/django-nunjucks/',
    license='LICENSE.txt',
    description='Django nunjucks tools.',
    long_description=open('README.rst').read(),
    install_requires=[
        #"Django >= 1.4.1",
    ],
)