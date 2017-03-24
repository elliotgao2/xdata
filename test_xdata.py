from xdata import *


class UserSchema(Schema):
    telephone = Str(max_length=12, min_length=16, requred=True)
    password = Str(max_length=12, min_length=16, requred=True)
    code = Str(length=4, requred=True)
