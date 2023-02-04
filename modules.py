# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime
from datetime import date
import time
from time import time

# Pip module
from camelcase import CamelCase

# Import custom module
import validator
from validator import validate_email

# today_sk = datetime.date.today()
today_sk = date.today()
timestamp_sk = time()

c_sk = CamelCase()
# print(c_sk.hump('hello there world'))

# print(timestamp_sk)

email_sk = 'test@test.com'
if validate_email(email_sk):
    print('Email is valid')
else:
    print('Email is bad')