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
    "ext": ".json",
    "langFolder": 'lang/',
})

print Language.get_path()

translated = Language.get('deliver_code', 'en', {'name': "John", 'code': 343923})

print translated


