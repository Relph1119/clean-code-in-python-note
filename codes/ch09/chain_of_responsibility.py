#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: chain_of_responsibility.py
@time: 2022/11/10 20:15
@project: clean-code-in-python-note
@desc: P274 职责链模式
事件系统，在日志记录行中，包含有关系统中发生事件的信息，提取这些信息
"""

import re
from typing import Optional, Pattern


class Event:
    pattern: Optional[Pattern[str]] = None

    def __init__(self, next_event=None):
        self.successor = next_event

    def process(self, logline: str):
        if self.can_process(logline):
            return self._process(logline)

        if self.successor is not None:
            return self.successor.process(logline)

    def _process(self, logline: str) -> dict:
        parsed_data = self._parse_data(logline)
        return {
            "type": self.__class__.__name__,
            "id": parsed_data["id"],
            "value": parsed_data["value"]
        }

    @classmethod
    def can_process(cls, logline: str) -> bool:
        return cls.pattern is not None and cls.pattern.match(logline) is not None

    @classmethod
    def _parse_data(cls, logline: str) -> dict:
        if not cls.pattern:
            return {}
        if (parsed := cls.pattern.match(logline)) is not None:
            return parsed.groupdict()
        return {}


class LoginEvent(Event):
    pattern = re.compile(r"(?P<id>\d+):\s+login\s+(?P<value>\S+)")


class LogoutEvent(Event):
    pattern = re.compile(r"(?P<id>\d+):\s+logout\s+(?P<value>\S+)")


class SessionEvent(Event):
    pattern = re.compile(r"(?P<id>\d+):\s+log(in|out)\s+(?P<value>\S+)")


if __name__ == '__main__':
    chain = LogoutEvent(LoginEvent())
    print(chain.process("567: login User1"))

    chain = SessionEvent(LoginEvent(LogoutEvent()))
    print(chain.process("798: login User2"))
