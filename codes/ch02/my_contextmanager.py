#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: my_contextmanager.py
@time: 2022/11/9 11:02
@project: clean-code-in-python-note
@desc: P29 实现上下文管理器
"""
import contextlib


def stop_database():
    print("stop database")


def start_database():
    print("start database")


@contextlib.contextmanager
def db_handler():
    try:
        stop_database()
        yield
    finally:
        start_database()


def db_backup():
    print("backup database")


if __name__ == '__main__':
    with db_handler():
        db_backup()
