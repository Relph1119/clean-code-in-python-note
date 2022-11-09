#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: my_sequence.py
@time: 2022/11/9 10:45
@project: clean-code-in-python-note
@desc: P25 创建自己的序列
"""
from collections.abc import Sequence


class Items(Sequence):
    def __init__(self, *value):
        self._values = list(value)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values.__getitem__(item)

    def __str__(self):
        return self._values.__str__()


if __name__ == '__main__':
    items = Items(2, 3, 4, 5)
    print("the 2nd item of Items is", items[2])
    print("Items: ", items)
