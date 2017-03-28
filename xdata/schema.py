from xdata.exceptions import CheckError
from xdata.types import DataType


class SchemaMeta(type):
    def __new__(mcs, name, bases, attrs):

        checkers = {}

        for k, v in attrs.items():
            if isinstance(v, DataType):
                checkers[k] = v

        for k in checkers:
            attrs.pop(k)

        attrs['checkers'] = checkers

        return super().__new__(mcs, name, bases, attrs)


class Schema(metaclass=SchemaMeta):
    def __init__(self, data):
        self.data = data
        self._validated_data = {}
        self._errors = {}
        self._checked = False
        self.valid = True
        self.validate()

    def validate(self):

        for k, v in self.checkers.items():
            self.checkers[k].name = k
            if k in self.data:
                self.checkers[k].value = self.data[k]

        for k, checker in self.checkers.items():
            result = checker.check()
            if result is None:
                self._validated_data[k] = self.checkers[k].value
            else:
                self._errors[k] = result

        if len(self._errors) != 0:
            self.valid = False

        self._checked = True

        return self

    @property
    def errors(self):

        if not self._checked:
            raise CheckError('Data should be validated before visit errors')

        if self.valid:
            raise CheckError('Data is valid')

        return self._errors

    @property
    def validated_data(self):

        if not self._checked:
            raise CheckError('Data should be validate before visit validated_data')

        if not self.valid:
            raise CheckError('Data is not valid')

        return self._validated_data
