#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


import Language


root_dir = os.path.split(__file__)[0]


Language.__({
    "default_lang": "en",
    "__basedir": root_dir,
})

Language.load('ar', {
    "deliver_code": "${name} إليك رمز otp ${code}"
})

Language.load('en', {
    "deliver_code": "Hello ${name}, here is your otp code ${code}"
})

translated = Language.get('deliver_code', 'ar', {'name': "John", 'code': 343923})

print(translated)

translated = Language.get('deliver_code', 'en', {'name': "John", 'code': 343923})

print(translated)
