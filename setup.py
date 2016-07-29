from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

long_description = ''
try:
    with open(path.join(here, 'README.rst')) as file:
        long_description = file.read()
except:
    pass

license = ''
try:
    with open(path.join(here, 'LICENSE.txt')) as file:
        license = file.read()
except:
    pass

setup(
    name='heapq_max',
    packages=['heapq_max'],
    version='0.21',
    description='A max Heap version of heapq module for Python.',
    author='Zhe He',
    author_email='hezhe88@gmail.com',
    url='https://github.com/he-zhe/heapq_max',
    download_url='https://github.com/he-zhe/heapq_max/archive/0.21.tar.gz',
    keywords=['heap', 'heapq', 'max heap'],
    classifiers=[],
    long_description=long_description,
    license=license
)
