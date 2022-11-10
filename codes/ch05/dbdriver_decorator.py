#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: dbdriver_decorator.py
@time: 2022/11/10 10:23
@project: clean-code-in-python-note
@desc: P147 创建在任何情况下都管用的装饰器
"""

from functools import wraps
from types import MethodType


class DBDriver:
    def __init__(self, dbstring: str) -> None:
        self.dbstring = dbstring

    def execute(self, query: str) -> str:
        return f"query {query} at {self.dbstring}"


class inject_db_driver:
    """Convert a string to a DBDriver instance and pass this to the wrapped function.
    """

    def __init__(self, function) -> None:
        self.function = function
        wraps(self.function)(self)

    def __call__(self, dbstring):
        return self.function(DBDriver(dbstring))

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return self.__class__(MethodType(self.function, instance))


@inject_db_driver
def run_query(driver):
    return driver.execute("test_function")


class DataHandler:
    @inject_db_driver
    def run_query(self, driver):
        return driver.execute(self.__class__.__name__)


if __name__ == '__main__':
    print(DataHandler().run_query("test_OK"))
