#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: validate_field.py
@time: 2022/11/10 11:26
@project: clean-code-in-python-note
@desc: P162 属性验证
"""
from typing import Any, Callable


class Validation:
    def __init__(self, validation_function: Callable[[Any], bool], error_msg: str) -> None:
        self.validation_function = validation_function
        self.error_msg = error_msg

    def __call__(self, value):
        if not self.validation_function(value):
            raise ValueError(f"{value!r} {self.error_msg}")


class Field:
    def __init__(self, *validations):
        self._name = None
        self.validations = validations

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]

    def validate(self, value):
        for validation in self.validations:
            validation(value)

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self._name] = value


class ClientClass:
    descriptor = Field(Validation(lambda x: isinstance(x, (int, float)), "is not a number"),
                       Validation(lambda x: x >= 0, "is not >= 0"))


if __name__ == '__main__':
    client = ClientClass()
    client.descriptor = 42
    print(client.descriptor)

    client.descriptor = -42
