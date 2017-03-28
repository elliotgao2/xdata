## Validate

```python
from xdata.schema import Schema
from xdata.types import *


class UserSchema(Schema):
    telephone = Str(length=11, required=True)
    password = Str(min_length=8,max_length=16, required=True)
    
request_data = {
    'telephone':'18180050000',
    'password':'idonotknow'
}

schema = UserSchema(request_data)
if schema.valid:
    print(schema.validated_data) # {'telephone': '18180050000', 'password': 'idonotknow'}
```
