## Errors

```python
from xdata.schema import Schema
from xdata.types import *

class UserSchema(Schema):
    telephone = Str(length=11, required=True)
    password = Str(min_length=8, max_length=16, required=True)


request_data = {}

schema = UserSchema(request_data)
if not schema.valid:
    print(schema.errors)  # {'telephone': 'telephone is required', 'password': 'password is required'}
```
