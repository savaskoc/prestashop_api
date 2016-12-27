from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='prestashop_api',
    version='0.0.1b1',

    description='Prestashop api wrapper for python',
    long_description=long_description,

    url='https://github.com/savaskoc/prestashop_api',

    author='Savas Koc',
    author_email='savaskoc11@gmail.com',

    license='Apache License 2.0',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='prestashop api',
    py_modules=["prestashop_api"],
    install_requires=['requests', 'xmltodict'],
)
