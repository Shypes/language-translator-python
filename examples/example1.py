import os
import sys
import inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from Language import Language

root_dir = os.path.split(__file__)[0]

LangParser = Language()

LangParser.set_base_dir(root_dir)

LangParser.set_active_lang('en')

print LangParser.get_path()

translated = LangParser.get('deliver_code', 'en', {'name': "John", 'code': 343923})

print(translated)

translated = LangParser.translate('something_went_wrong')

print(translated)

translated = LangParser.translate('missing_required_validation')

print(translated)

translated = LangParser.translate('email_phone_validation')

print(translated)