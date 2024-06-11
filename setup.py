import setuptools

with open('README.md','r') as file:
    long_description = file.read()

setuptools.setup(name = 'preprocess_kgptalkie', # this should be unique from e.x github
version = '0.0.1',
author = 'endzii',
author_email = 'andziaj147@gmail.com' ,
description= 'this is a preprocessing package' ,
long_description = long_description,
long_description_content_type = 'text/markdown' ,
packages='requirements.txt',
classifiers = ['Programming Language :: Python :: 3',
               'Licence :: OSI Approved :: MIT Licence',
               "Operating System :: Windows"],
python_requires = '>=3.5')

