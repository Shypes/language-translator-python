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


def test_translate(language, message):

    translated = LangParser.translate(message, language)
    data = {
        "message": translated,
        "language": language
    }

    print (data)


test_translate('ar', 'success')

test_translate('ar', 'something_went_wrong')

test_translate('ar', 'missing_required_validation')

test_translate('ar', 'email_phone_validation')


