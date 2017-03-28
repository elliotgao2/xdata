## DataTypes

```python
from xdata.schema import Schema
from xdata.types import *

DataType(required=True,default='11',choices=[])

Str(length=11, max_length=12,min_length=10,regex="")
Int(max=10000,min=12)
Bool(max=10000,min=12)
Decimal(left=5,right=2)
DateTime(max_datetime='2001-01-01 00:00:00', min_datetime='2000-01-01 00:00:00')
Date(max_date='2001-01-01', min_date='2000-01-01')
Time(max_time='06:00:00', min_time='05:00:00')

```
