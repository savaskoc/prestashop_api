prestashop_api
==============
[![PyPI version](https://badge.fury.io/py/prestashop_api.svg)](https://badge.fury.io/py/prestashop_api)

prestashop_api is a library for Python 2 and 3 to interact with the PrestaShop's Web Service API.

Learn more about the PrestaShop Web Service from the [Official Prestashop Documentation].

prestashop_api is a thin wrapper around the PrestaShop Web Service:
it takes care of making the call to your PrestaShop instance's Web Service,
supports the Web Service's HTTP-based CRUD operations (handling any errors)
and then returns the result ready for you to work with in Python (via xmltodict)


Installation
============

The easiest way to install prestashop_api using pip:

    pip install prestashop_api

If you do not have setuptools, clone repo from [Source], unzip it and run:

    python setup.py install


Usage
=====

see [example.py]

API Documentation
=================

Documentation for the PrestaShop Web Service can be found on the
PrestaShop wiki: [Using the REST webservice]


Credits:
========

Thanks to Prestashop SA for their PHP API Client PSWebServiceLibrary.php


Copyright and License
=====================

Copyright 2016 Savas Koc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


[Official Prestashop Documentation]: http://doc.prestashop.com/display/PS16/Using+the+PrestaShop+Web+Service
[Using the REST webservice]: http://doc.prestashop.com/display/PS16/Using+the+PrestaShop+Web+Service
[Source]: https://github.com/savaskoc/prestashop_api
[example.py]: example.py
