#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: borg.py
@time: 2022/11/10 19:29
@project: clean-code-in-python-note
@desc: P265 Borg模式
"""
import logging


class SharedAllMixin:
    def __init__(self, *args, **kwargs):
        try:
            self.__class__._attributes
        except AttributeError:
            self.__class__._attributes = {}

        self.__dict__ = self.__class__._attributes
        super().__init__(*args, **kwargs)


class BaseFetcher:
    def __init__(self, source):
        self.source = source


class TagFetcher(SharedAllMixin, BaseFetcher):
    def pull(self):
        logging.info("pulling from tag %s", self.source)
        return f"Tag = {self.source}"


class BranchFetch(SharedAllMixin, BaseFetcher):
    def pull(self):
        logging.info("pulling from branch %s", self.source)
        return f"Branch = {self.source}"

