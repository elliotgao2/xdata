"""
Custom Schema class should be a subclass of Schema
"""

from xdata.exceptions import CheckError
from xdata.types import DataType


class SchemaMeta(type):
    """
    SchemaMeta is for init the checkers of a custom Schema
    """

    def __new__(mcs, name, bases, attrs):

        checkers = {}

        for k, checker in attrs.items():
            if isinstance(checker, DataType):
                checkers[k] = checker
                checker.name = k

        for k in checkers:
            attrs.pop(k)

        attrs['checkers'] = checkers

        return super().__new__(mcs, name, bases, attrs)


class Schema(metaclass=SchemaMeta):
    """
    Schema is the base class of custom Schema
    """

    def __init__(self, data):
        self.data = data
        self._validated_data = {}
        self._errors = {}
        self._checked = False
        self.valid = True
        self.validate()
        self.checkers = self.checkers

    def validate(self):
        """
        Validate all data.
        """
        for k, checker in self.checkers.items():

            if k in self.data:
                checker.value = self.data[k]

        for k, checker in self.checkers.items():
            result = checker.valid()
            if result is True:
                self._validated_data[k] = checker.value
            else:
                self._errors[k] = result

        if len(self._errors) != 0:
            self.valid = False

        self._checked = True

        return self

    @property
    def errors(self):
        """
        Return errors as a dict
        """
        if not self._checked:
            raise CheckError('Data should be validated before visit errors')

        if self.valid:
            raise CheckError('Data is valid')

        return self._errors

    @property
    def validated_data(self):
        """
        Return validated_data as a dict
        """
        if not self._checked:
            raise CheckError('Data should be validate before visit validated_data')

        if not self.valid:
            raise CheckError('Data is not valid')

        return self._validated_data
