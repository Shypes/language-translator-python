#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from Language import Language

root_dir = os.path.split(__file__)[0]

Language = Language({
    "default_lang": "en",
    "__basedir": root_dir,
})


Language.load('ar', {
    "data": "البيانات",
    "message": "رسالة",
})


def test_translate(res, content, message):

    response_data = {"message": "", "param": ""}

    if isinstance(message, str):
        response_data['message'] = message
        message = {}

    response_data.update(message)

    translated = Language.get(response_data['message'], res['language'], response_data['param'])

    lang_key = False if res['lang_key'] is False else True

    response_key = {
        'data': Language.text('data') if lang_key is True else 'data',
        'message': Language.text('message') if lang_key is True else 'message',
        'success': Language.text('success') if lang_key is True else 'success'
    }

    data = {
        response_key['success']: True,
        response_key['message']: translated,
        response_key['data']: content
    }

    print(data)


res = {
    'language': 'ar',
    'lang_key': True
}

test_translate(res, [], 'success')

test_translate(res, [], 'something_went_wrong')

test_translate(res, [], 'missing_required_validation')

test_translate(res, [], 'email_phone_validation')

