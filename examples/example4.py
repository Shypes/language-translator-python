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

translate = LangParser.init('ar')

print(LangParser.get_text('missing_truck', 'ar', {'status': "delivered"}))

print(LangParser.get_text('something_went_wrong'))

print(LangParser.get_text('missing_required_validation'))

print(LangParser.get_text('email_phone_validation'))

