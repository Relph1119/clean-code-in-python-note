#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: func_convert_method.py
@time: 2022/11/10 13:54
@project: clean-code-in-python-note
@desc: P184 将函数转换为方法
"""
from types import MethodType


class Method:
    def __init__(self, name):
        self.name = name

    def __call__(self, instance, arg1, arg2):
        print(f"{self.name}: {instance} called with {arg1} and {arg2}")

    def __get__(self, instance, owner):
        if instance is None:
            return self
        # 将函数转换为方法
        return MethodType(self, instance)


class MyClass:
    method = Method("Internal call")


if __name__ == '__main__':
    instance = MyClass()
    Method("External call")(instance, "first", "second")
    instance.method("first", "second")
