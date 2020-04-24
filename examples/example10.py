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

Language.set_safe_load(False)

def run():

    Language.set_load_from_file(False)

    Language.load('ar', {
        "deliver_code": "why مرحبًا ${name} ، إليك رمز me ${code}"
    })

    Language.load('en', {
        "deliver_code": "why ${name}, here is your me code ${code}"
    })

    print(Language.get_path())

    translated = Language.get('deliver_code', 'ar', {'name': "John", 'code': 343923})

    print(translated)

    translated = Language.get('deliver_code','en', {'name': "John", 'code': 343923})

    print(translated)

    Language.set_load_from_file(True)

    Language.set_language_dir("lang/email")

    print(Language.get_path())

    translated = Language.get('deliver_code', 'ar', {'name':"John", 'code': 343923})

    print(translated)

    translated = Language.get('deliver_code','en', {'name':"John", 'code': 343923})

    print(translated)

    Language.set_language_dir("lang")

    print(Language.get_path())

    translated = Language.get('deliver_code','ar', {'name':"John", 'code': 343923})

    print(translated)

    translated = Language.get('deliver_code','en', {'name':"John", 'code': 343923})

    print(translated)

    Language.set_language_dir("lang/email")

    print(Language.get_path())

    translated = Language.get('deliver_code','ar', {'name':"John", 'code': 343923})

    print(translated)

    translated = Language.get('deliver_code','en', {'name':"John", 'code': 343923})

    print(translated)

    Language.load('ar', {
        "deliver_code": "مرحبًا ${name} ، إليك رمز fuck ${code}"
    })

    Language.load('en', {
        "deliver_code": "Hello ${name}, here is your me fuck ${code}"
    })

    print(Language.get_path())

    translated = Language.get('deliver_code','ar', {'name':"John", 'code': 343923})

    print(translated)

    translated = Language.get('deliver_code','en', {'name':"John", 'code': 343923})

    print(translated)

    Language.set_language_dir("lang")

    print(Language.get_path())

    translated = Language.get('deliver_code', 'ar', {'name': "John", 'code': 343923})

    print(translated)

    translated = Language.get('deliver_code', 'en', {'name': "John", 'code': 343923})

    print(translated)

    Language.set_language_dir("lang/email")

    print(Language.get_path())

    translated = Language.get('deliver_code', 'ar', {'name': "John", 'code': 343923})

    print(translated)

    translated = Language.get('deliver_code', 'en', {'name': "John", 'code': 343923})

    print(translated)

    translated = Language.get('deliver_code_me', 'ar', {'name': "John", 'code': 343923})

    print(translated)

    translated = Language.get('deliver_code_me', 'en', {'name': "John", 'code': 343923})

    print(translated)


run()








 


