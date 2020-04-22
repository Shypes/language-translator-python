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

LangParser = Language()

LangParser.set_base_dir(root_dir)

LangParser.set_active_lang('ar')

LangParser.set_load_from_file(False)

LangParser.load('en', {
   "success": "Success!",
   "email_phone_validation": "Email and phone cannot be empty",
   "something_went_wrong": "Something went wrong!",
   "missing_required_validation": "Missing required fields",
   "missing_truck": "Truck Request Pool has already been set to ${status}",
   "deliver_code":"Hello ${name}, here is your otp code ${code}",
   "John": "John",
})

LangParser.load('ar', {
   "success": "نجاح",
   "email_phone_validation": "لا يمكن أن يكون البريد الإلكتروني والهاتف فارغين",
   "something_went_wrong": "هناك خطأ ما!",
   "missing_required_validation": "الحقول المطلوبة مفقودة",
   "missing_truck": "تم تعيين تجمع طلبات الشاحنات بالفعل على {status}$",
   "deliver_code": "${name} إليك رمز otp ${code}",
   "John": "نجاح",
})

translated = LangParser.translate('deliver_code', 'ar', {'name': "John", 'code': 343923})

print(translated)

translated = LangParser.translate('deliver_code', 'en', {'name': "John", 'code': 343923})

print(translated)
