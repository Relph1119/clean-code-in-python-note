#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: ext_inner_type.py
@time: 2022/11/9 13:55
@project: clean-code-in-python-note
@desc: P53 扩展内置类型
"""
from collections import UserList


class GoodList(UserList):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if index % 2 == 0:
            prefix = "even"
        else:
            prefix = "odd"
        return f"[{prefix} {value}]"


if __name__ == '__main__':
    g1 = GoodList((0, 1, 2))
    print("g1[0] =", g1[0])
    print("g1[1] =", g1[0])
    print(", ".join(g1))
