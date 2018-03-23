# -*- coding: utf-8 -*-
from distutils.core import setup, Extension

setup (name = 'pciutils',
       version = '2.3.7',
       description = 'Interface to hwdata',
       author = 'Miroslav Suchý',
       author_email = 'msuchy@redhat.com',
       license = 'GPLv2',
       url = 'https://github.com/xsuchy/python-hwdata',
       py_modules = ['hwdata'])
