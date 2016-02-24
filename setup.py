from distutils.core import setup

setup(
    name='EveMatcher',
    version='',
    packages=['Frontend', 'Frontend.migrations', 'Matching', 'Matching.migrations', 'EveMatcher', 'RestEveXML',
              'RestEveXML.migrations', 'RestEveCrest', 'RestEveCrest.migrations'],
    url='',
    license='',
    author='',
    author_email='',
    description='',
    install_requires=[
        'Django',
        'djangorestframework',
        'pycrest',
        'evelink',
    ]
)
