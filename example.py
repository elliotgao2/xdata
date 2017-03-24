from xdata import *


class UserSchema(Schema):
    telephone = Str(length=11, required=True)
    password = Str(min_length=8, max_length=16, required=True)


request_data = {
    'telephone': '18180050000',
    'password': 'idonotknow'
}
schema = UserSchema(request_data)
schema.validate()
if schema.valid:
    print(schema.validated_data)  # {'telephone': '18180050000', 'password': 'idonotknow'}


class UserSchema(Schema):
    telephone = Str(length=11, required=True)
    password = Str(min_length=8, max_length=16, required=True)


request_data = {}

schema = UserSchema(request_data)
if not schema.valid:
    print(schema.errors)  # {'telephone': 'telephone is required', 'password': 'password is required'}
