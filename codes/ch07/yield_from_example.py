#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: yield_from_example.py
@time: 2022/11/10 16:48
@project: clean-code-in-python-note
@desc: P212 yield from新语法
"""


def chain(*iterables):
    for it in iterables:
        yield from it


if __name__ == '__main__':
    l = list(chain("hello", ["world"], ("tuple", " of ", "values.")))
    print(l)
