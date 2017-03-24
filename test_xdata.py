from xdata import *


def test_required():
    class UserSchema(Schema):
        telephone = Str(length=11, required=True)

    data = {}

    assert 'telephone' in UserSchema(data).errors


def test_default():
    class UserSchema(Schema):
        telephone = Str(default='1234')

    data = {}

    assert UserSchema(data).validated_data['telephone'] == '1234'


def test_choices():
    class UserSchema(Schema):
        telephone = Str(choices=['a', 'b'])

    assert 'telephone' in UserSchema({}).errors
    assert 'telephone' in UserSchema({'telephone': '1'}).errors
    assert 'telephone' in UserSchema({'telephone': 'a'}).validated_data


def test_fn():
    class UserSchema(Schema):
        telephone = Str(fn=lambda s: 10 < len(s) <= 12)

    assert 'telephone' in UserSchema({}).errors
    assert 'telephone' in UserSchema({'telephone': '1'}).errors
    assert 'telephone' in UserSchema({'telephone': '12345678901'}).validated_data


def test_str_length_range():
    class UserSchema(Schema):
        telephone = Str(max_length=8, min_length=5)

    assert 'telephone' in UserSchema({}).errors
    assert 'telephone' in UserSchema({'telephone': '1'}).errors
    assert 'telephone' in UserSchema({'telephone': '123456789'}).errors
    assert 'telephone' in UserSchema({'telephone': '1234567'}).validated_data


def test_str_length():
    class UserSchema(Schema):
        password = Str(length=8)

    assert 'password' in UserSchema({'password': '1234567809'}).errors
    assert 'password' in UserSchema({'password': '1234569'}).errors
    assert 'password' in UserSchema({'password': '12345678'}).validated_data


def test_int_range():
    class UserSchema(Schema):
        password = Int(max=8, min=3)

    assert 'password' in UserSchema({'password': '1234567809'}).errors
    assert 'password' in UserSchema({'password': 12312321312321}).errors
    assert 'password' in UserSchema({'password': 2}).errors
    assert 'password' in UserSchema({'password': 5}).validated_data


def test_bool():
    class UserSchema(Schema):
        is_active = Bool()

    assert 'is_active' in UserSchema({'is_active': '1234567809'}).errors
    assert 'is_active' in UserSchema({'is_active': 12312321312321}).errors
    assert 'is_active' in UserSchema({'is_active': True}).validated_data
    assert 'is_active' in UserSchema({'is_active': False}).validated_data


def test_decimal():
    class UserSchema(Schema):
        money = Decimal(left=4, right=2)

    assert 'money' in UserSchema({'money': '1234567809'}).errors
    assert 'money' in UserSchema({'money': 222.1}).errors
    assert 'money' in UserSchema({'money': 22222.1}).errors
    assert 'money' in UserSchema({'money': 2222.22}).validated_data


def test_datetime():
    class UserSchema(Schema):
        birthday = DateTime(max_datetime='2001-01-01 00:00:00', min_datetime='2000-01-01 00:00:00')

    assert 'birthday' in UserSchema({'birthday': '1234567809'}).errors
    assert 'birthday' in UserSchema({'birthday': 222.1}).errors
    assert 'birthday' in UserSchema({'birthday': 22222.1}).errors
    assert 'birthday' in UserSchema({'birthday': '1999-01-01 00:00:00'}).errors
    assert 'birthday' in UserSchema({'birthday': '2002-01-01 00:00:00'}).errors
    assert 'birthday' in UserSchema({'birthday': '2000-02-01 00:00:00'}).validated_data


def test_date():
    class UserSchema(Schema):
        birthday = Date(max_date='2001-01-01', min_date='2000-01-01')

    assert 'birthday' in UserSchema({'birthday': '1234567809'}).errors
    assert 'birthday' in UserSchema({'birthday': 222.1}).errors
    assert 'birthday' in UserSchema({'birthday': 22222.1}).errors
    assert 'birthday' in UserSchema({'birthday': '1999-01-01'}).errors
    assert 'birthday' in UserSchema({'birthday': '2002-01-01'}).errors
    assert 'birthday' in UserSchema({'birthday': '2000-02-01'}).validated_data


def test_time():
    class UserSchema(Schema):
        birthday = Time(max_time='06:00:00', min_time='05:00:00')

    assert 'birthday' in UserSchema({'birthday': '1234567809'}).errors
    assert 'birthday' in UserSchema({'birthday': 222.1}).errors
    assert 'birthday' in UserSchema({'birthday': 22222.1}).errors
    assert 'birthday' in UserSchema({'birthday': '00:00:00'}).errors
    assert 'birthday' in UserSchema({'birthday': '02:00:00'}).errors
    assert 'birthday' in UserSchema({'birthday': '05:50:00'}).validated_data
