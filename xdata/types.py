import re
from datetime import datetime


class DataType:
    def __init__(self, *args, **kwargs):
        self.required = kwargs.get('required', False)
        self.default = kwargs.get('default', None)
        self.choices = kwargs.get('choices', None)
        self.fn = kwargs.get('fn', None)
        self.value = None
        self.name = None

    def check(self):
        if self.default is not None and not self.required:
            self.value = self.default

        if self.required and self.value is None:
            return '{} is required'.format(self.name)

        if self.choices is not None and self.value not in self.choices:
            return '{} should be in [{}]'.format(self.name, ','.join(self.choices))

        if self.fn is not None and self.value is not None and not self.fn(self.value):
            return '{} should be satisfied function {}'.format(self.name, self.fn)


class Str(DataType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_length = kwargs.get('max_length', None)
        self.min_length = kwargs.get('min_length', None)
        self.length = kwargs.get('length', None)
        self.regex = kwargs.get('regex', None)

    def check(self):
        result = super().check()
        if result is not None:
            return result

        if not isinstance(self.value, str):
            return 'type of {} should be string'.format(self.name)

        if self.min_length is not None and len(self.value) < self.min_length:
            return 'length of {} should be larger than {}'.format(self.name, self.min_length)

        if self.max_length is not None and len(self.value) > self.max_length:
            return 'length of {} should be less than {}'.format(self.name, self.max_length)

        if self.length is not None and len(self.value) != self.length:
            return 'length of {} should be equal to {}'.format(self.name, self.length)

        if self.regex is not None and re.compile(self.regex).match(self.value):
            return '{} should match with regex "{}"'.format(self.name, self.regex)


class Int(DataType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max = kwargs.get('max', None)
        self.min = kwargs.get('min', None)

    def check(self):
        result = super().check()
        if result is not None:
            return result

        if not isinstance(self.value, int):
            return 'type of {} should be integer'.format(self.name)

        if self.max is not None and self.value > self.max:
            return '{} should be less than {}'.format(self.name, self.max)

        if self.min is not None and self.value < self.min:
            return '{} should be larger than {}'.format(self.name, self.min)


class Bool(DataType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def check(self):
        super().check()
        if not isinstance(self.value, bool):
            return 'type of {} should be boolean'.format(self.name)


class Decimal(DataType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.left = kwargs.get('left', 8)
        self.right = kwargs.get('right', 2)

    def check(self):
        result = super().check()
        if result is not None:
            return result
        if not isinstance(self.value, float):
            return 'type of {} should be decimal'.format(self.name)

        point_left, point_right = str(self.value).split('.')

        if len(point_left) > self.left:
            return 'length of the right of the decimal point should be less than {}'.format(self.left)
        if not len(point_right) == self.right:
            return 'length of the left of the decimal point should be equal to {}'.format(self.right)


class DateTime(DataType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_datetime = kwargs.get('max_datetime', None)
        self.min_datetime = kwargs.get('min_datetime', None)

        self.max_datetime = datetime.strptime(self.max_datetime, "%Y-%m-%d %H:%M:%S")
        self.min_datetime = datetime.strptime(self.min_datetime, "%Y-%m-%d %H:%M:%S")

    def check(self):
        result = super().check()
        if result is not None:
            return result

        try:
            self.value = datetime.strptime(self.value, "%Y-%m-%d %H:%M:%S")
        except (ValueError, TypeError):
            return '{} should be right datetime'.format(self.name)

        if self.value > self.max_datetime:
            return '{} should be before {}'.format(self.name, self.max_datetime)
        if self.value < self.min_datetime:
            return '{} should be after {}'.format(self.name, self.min_datetime)


class Date(DataType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_date = kwargs.get('max_date', None)
        self.min_date = kwargs.get('min_date', None)

        self.max_date = datetime.strptime(self.max_date, "%Y-%m-%d")
        self.min_date = datetime.strptime(self.min_date, "%Y-%m-%d")

    def check(self):
        result = super().check()
        if result is not None:
            return result

        try:
            self.value = datetime.strptime(self.value, "%Y-%m-%d")
        except (ValueError, TypeError):
            return '{} should be right date'.format(self.name)

        if self.value > self.max_date:
            return '{} should be before {}'.format(self.name, self.max_date)
        if self.value < self.min_date:
            return '{} should be after {}'.format(self.name, self.min_date)


class Time(DataType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_time = kwargs.get('max_time', None)
        self.min_time = kwargs.get('min_time', None)

        self.max_time = datetime.strptime(self.max_time, "%H:%M:%S")
        self.min_time = datetime.strptime(self.min_time, "%H:%M:%S")

    def check(self):
        result = super().check()
        if result is not None:
            return result

        try:
            self.value = datetime.strptime(self.value, "%H:%M:%S")
        except (ValueError, TypeError):
            return '{} should be right time'.format(self.name)
        if self.value > self.max_time:
            return '{} should be before {}'.format(self.name, self.max_time)
        if self.value < self.min_time:
            return '{} should be after {}'.format(self.name, self.min_time)
