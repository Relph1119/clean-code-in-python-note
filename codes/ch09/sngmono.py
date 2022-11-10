#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: sngmono.py
@time: 2022/11/10 19:19
@project: clean-code-in-python-note
@desc: P263~P264 单态模式
假设有一个对象，它必须根据标签指定的版本号合并Git仓库中某些代码的相应版本。
这个对象可能有多个实例，每当客户端调用获取代码的方法时，这个对象都将使用标签确定最新的版本。
"""
import logging


class SharedAttribute:
    def __init__(self, initial_value=None):
        self.value = initial_value
        self._name = None

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.value is None:
            raise AttributeError(f"{self._name} was never set")
        return self.value

    def __set__(self, instance, new_value):
        self.value = new_value

    def __set_name__(self, owner, name):
        self._name = name


class GitFetcher:
    current_tag = SharedAttribute()
    current_branch = SharedAttribute()

    def __init__(self, tag, branch=None):
        self.current_branch = branch
        self.current_tag = tag

    def pull(self):
        logging.info("pulling from %s", self.current_tag)
        return self.current_tag


if __name__ == '__main__':
    f1 = GitFetcher(0.1)
    f2 = GitFetcher(0.2)
    f1.current_tag = 0.3
    print("f2 pull, the tag is", f2.pull())
    print("f1 pull, the tag is", f1.pull())
