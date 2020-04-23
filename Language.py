__author__ = 'Adesipe Tosin'

import os
import json
import re
from functools import partial


class Language:
    FolerLanguage = {}
    LanguageData = {}

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
        if self.option['langFolder'] != directory:
            self.option['langFolder'] = directory
            self.set_path()
            self.init(False)
            for language in self.FolerLanguage[self.option['langFolder']]:
                data = self.FolerLanguage[self.option['langFolder']][language]
                self.load(language, data)

    def set_default_lang(self, language):
        self.option['default_lang'] = language
        self.loaded = False
        self.defaultLangData = {}

    def set_path(self):
        self.langPath = self.option['__basedir'] + '/' + self.option['langFolder']
        if self.option['langFolder'] not in self.FolerLanguage:
            self.FolerLanguage[self.option['langFolder']] = {}

    def get_path(self):
        return self.langPath

    def text(self, text, language='', param={}):
        language = language if (language and language != '' and isinstance(language, str)) else self.active_lang
        if language in self.LanguageData:
            if text in self.LanguageData[language]:
                if len(param) == 0:
                    return self.LanguageData[language][text]
                else:
                    return self.render_string(self.LanguageData[language][text], param)
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

    def load_default_lang(self):
        if self.loaded is False:
            self.load_language(self.option['default_lang'])
        self.loaded = True

    def load_active_lang(self):
        self.load_language(self.active_lang)

    def has_loaded_language(self, language):
        return language in self.FolerLanguage[self.option['langFolder']]

    def can_load(self, language):
        file_path = self.get_path()
        return os.path.exists(file_path + '/' + language + self.option['ext'])

    def mark_as_loaded(self, language):
        self.load_folder_language(language)

    def load_folder_language(self, language, data={}):
        if isinstance(data, dict):
            self.set_path()
            self.FolerLanguage[self.option['langFolder']][language] = data

    def get_folder_language(self, language):
        if self.option['langFolder'] in self.FolerLanguage:
            if language in self.FolerLanguage[self.option['langFolder']]:
                return self.FolerLanguage[self.option['langFolder']][language]
        return {}

    def get_file(self, language):
        file_path = self.get_path()
        with open(file_path + '/' + language + self.option['ext']) as data_file:
            try:
                return json.load(data_file)
            except Exception:
                return {}

    def load_language(self, language):
        if self.load_from_file and not self.has_loaded_language(language):
            if self.can_load(language):
                self.load_folder_language(language, self.get_file(language))
                self.load(language, self.get_folder_language(language))
            else:
                self.mark_as_loaded(language)

    def load(self, language, data):
        if isinstance(data, dict) and len(data) > 0:
            if language not in self.LanguageData:
                self.LanguageData[language] = data.copy()
            else:
                self.LanguageData[language].update(data)


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


def set_load_from_file(load):
    Lang = getLang()
    return Lang.set_load_from_file(load)


def get_path():
    Lang = getLang()
    return Lang.get_path()


def set_language_dir (directory):
    Lang = getLang()
    return Lang.set_language_dir (directory)
