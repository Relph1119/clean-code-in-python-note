#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: with_params_decorator.py
@time: 2022/11/10 10:02
@project: clean-code-in-python-note
@desc: P134 指定参数默认值的装饰器
"""
from functools import partial, wraps

DEFAULT_X = 1
DEFAULT_Y = 1


def decorator(function=None, *, x=DEFAULT_X, y=DEFAULT_Y):
    if function is None:
        return partial(decorator, x=x, y=y)

    @wraps(function)
    def wrapped():
        return function(x, y)

    return wrapped


@decorator(x=3, y=4)
def my_function(x, y):
    return x + y


if __name__ == '__main__':
    print("ans =", my_function())
