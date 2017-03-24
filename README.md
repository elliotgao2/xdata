# XData

A simple but useful library for validating data.
Most of the situation is validating request data.

## Features

- Easy to use, only one step
- Easy to extend
- No dependencies

## Required

- python >= 3.5

## Installation

`pip install xdata`

## Usage

### Validated_data

```python
from xdata import *

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

### Errors

```python
from xdata import *

class UserSchema(Schema):
    telephone = Str(length=11, required=True)
    password = Str(min_length=8, max_length=16, required=True)


request_data = {}

schema = UserSchema(request_data)
if not schema.valid:
    print(schema.errors)  # {'telephone': 'telephone is required', 'password': 'password is required'}
```

### DataTypes

```python
from xdata import *

DataType(required=True,default='11',choices=[])

Str(length=11, max_length=12,min_length=10,regex="")
Int(max=10000,min=12)
Bool(max=10000,min=12)
Decimal(left=5,right=2)
DateTime(max_datetime='2001-01-01 00:00:00', min_datetime='2000-01-01 00:00:00')
Date(max_date='2001-01-01', min_date='2000-01-01')
Time(max_time='06:00:00', min_time='05:00:00')

```

## Test

`coverage run --source=xdata -m pytest && coverage report`


## Todos

1. More DateTypes
2. More Check rules

## License

MIT