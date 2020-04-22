__author__ = 'Adesipe Tosin'

import os
import json
import re
from functools import partial


class Language:
    activeLangData = {}
    defaultLangData = {}
    passiveLangData = {}

    option = {}
    default = {
        "default_lang": "en",
        "__basedir": "./",
        "ext": ".json",
        "langFolder": 'lang',
    }
    active_lang = ''
    loaded = False
    load_from_file = False
    langPath = ""

    def __init__(self, options={}):
        self.reset(options)

    def set_options(self, options):
        self.option = self.default.copy()
        self.option.update(options)

    def reset(self, options):
        self.set_options(options)
        self.active_lang = self.option['default_lang']
        self.loaded = False
        self.load_from_file = True
        self.set_path()

    def set_active_lang(self, language):
        language = language if (language and language != '' and isinstance(language, str)) else ''
        if language != '':
            self.active_lang = language.strip()

    def set_extension(self, ext):
        self.option['ext'] = ext

    def set_load_from_file(self, is_load):
        self.load_from_file = False if is_load is False else True

    def set_base_dir(self, directory):
        self.option['__basedir'] = directory
        self.set_path()

    def set_language_dir(self, directory):
        self.option['langFolder'] = directory
        self.set_path()

    def set_default_lang(self, language):
        self.option['default_lang'] = language
        self.loaded = False
        self.defaultLangData = {}

    def set_path(self):
        self.langPath = self.option['__basedir'] + '/' + self.option['langFolder']

    def get_path(self):
        return self.langPath

    def text(self, text, language='', param={}):
        language = language if (language and language != '' and isinstance(language, str)) else self.active_lang
        if language in self.passiveLangData:
            if text in self.passiveLangData[language]:
                if len(param) == 0:
                    return self.passiveLangData[language][text]
                else:
                    return self.render_string(self.passiveLangData[language][text], param)
        return text

    def get_text(self, text, language='', param={}):
        return self.text(text, language, param)

    @staticmethod
    def evaluate(variables, match):
        found = match.group(1)
        item = variables[found] if found in variables else found
        return str(item)

    def render_string(self, template, variables):
        return re.sub('\$\{(.+?)\}', partial(self.evaluate, variables), template)

    def translate(self, text, language='', param={}):
        self.init(language)
        return self.text(text, language, param)

    def get(self, text, language='', param={}):
        return self.translate(text, language, param)

    def init(self, language):
        self.set_active_lang(language)
        self.load_default_lang()
        self.load_active_lang()
        self.load_passive_lang()

    def load_default_lang(self):
        if len(self.defaultLangData) == 0 \
                and self.loaded is False \
                and self.load_from_file:
            file_path = self.get_path()
            is_file = os.path.exists(file_path + '/' + self.option['default_lang'] + self.option['ext'])
            if is_file:
                with open(file_path + '/' + self.option['default_lang'] + self.option['ext']) as data_file:
                    try:
                        self.defaultLangData = json.load(data_file)
                    except Exception:
                        self.defaultLangData = {}
            else:
                self.defaultLangData = {}
        self.loaded = True

    def load_active_lang(self):
        if (self.active_lang not in self.activeLangData) \
                and self.load_from_file \
                and (self.active_lang not in self.passiveLangData):
            if self.option['default_lang'] == self.active_lang:
                self.activeLangData[self.active_lang] = self.defaultLangData.copy()
            else:
                file_path = self.get_path()
                is_file = os.path.exists(file_path + '/' + self.active_lang + self.option['ext'])
                if is_file:
                    with open(file_path + '/' + self.active_lang + self.option['ext']) as data_file:
                        try:
                            self.activeLangData[self.active_lang] = json.load(data_file)
                        except Exception:
                            self.activeLangData[self.active_lang] = {}
                else:
                    self.activeLangData[self.active_lang] = {}

    def load_passive_lang(self):
        if self.active_lang not in self.passiveLangData:
            self.passiveLangData[self.active_lang] = self.defaultLangData.copy()
            if self.active_lang in self.activeLangData:
                self.passiveLangData[self.active_lang].update(self.activeLangData[self.active_lang])

    def load(self, language, data):
        if language not in self.passiveLangData:
            self.passiveLangData[language] = data.copy()
        else:
            self.passiveLangData[language].update(data)

    def load_language(self, language, data):
        return self.load(language, data)


_SL = None


def getLang (options={}):
    global _SL
    if _SL is None:
        _SL = Language(options)
    return _SL


def __(options={}):
    return getLang(options)


def get(text, language='', param={}):
    Lang = getLang()
    return Lang.get(text, language, param)


def text(text, language='', param={}):
    Lang = getLang()
    return Lang.text(text, language, param)


def load(language, data):
    Lang = getLang()
    Lang.init(language)
    return Lang.load(language, data)



