from xdata.schema import Schema
from xdata.types import *


class UserSchema(Schema):
    username = Str()


schema = UserSchema({'username': '1234567890'})
if schema.valid:
    print(schema.validated_data)
else:
    print(schema.errors)
