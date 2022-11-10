#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: decorator.py
@time: 2022/11/10 20:05
@project: clean-code-in-python-note
@desc: P270 装饰器模式
查询结果生成对象的简化版，以字典的方式返回传递给它的参数。
在最简单的情况下，查询对象只是返回一个字典，其中包含通过参数传递给它的数据。
"""


class DictQuery:
    def __init__(self, **kwargs):
        self._raw_query = kwargs

    def render(self) -> dict:
        return self._raw_query


class QueryEnhancer:
    def __init__(self, query: DictQuery):
        self.decorated = query

    def render(self):
        return self.decorated.render()


class RemoveEmpty(QueryEnhancer):
    def render(self):
        original = super().render()
        return {k: v for k, v in original.items() if v}


class CaseInsensitive(QueryEnhancer):
    def render(self):
        original = super().render()
        return {k: v.lower() for k, v in original.items()}


if __name__ == '__main__':
    original = DictQuery(key="value", empyt="", none=None, upper="UPPERCASE", title="Title")
    new_query = CaseInsensitive(RemoveEmpty(original))
    print("original is", original.render())
    print("new query is", new_query.render())
