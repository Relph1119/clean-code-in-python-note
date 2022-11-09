#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: system_monitor_openclosed1.py
@time: 2022/11/9 15:50
@project: clean-code-in-python-note
@desc: P102 监视系统的原始代码
"""
from dataclasses import dataclass


@dataclass
class Event:
    raw_data: dict


class UnknownEvent(Event):
    """A type of event that cannot be identified from its data."""


class LoginEvent(Event):
    """An event repressenting a user that has just entered the system."""


class LogoutEvent(Event):
    """An event representing a user that has just left the system."""


class SystemMonitor:
    """Identify events that occurred in the system."""

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        if self.event_data["before"]["session"] == 0 and self.event_data["after"]["session"] == 1:
            return LoginEvent(self.event_data)
        elif self.event_data["before"]["session"] == 1 and self.event_data["after"]["session"] == 0:
            return LogoutEvent(self.event_data)

        return UnknownEvent(self.event_data)


if __name__ == '__main__':
    l1 = SystemMonitor({"before": {"session": 0}, "after": {"session": 1}})
    print("the current event is", l1.identify_event().__class__.__name__)

    l2 = SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
    print("the current event is", l2.identify_event().__class__.__name__)

    l3 = SystemMonitor({"before": {"session": 1}, "after": {"session": 1}})
    print("the current event is", l3.identify_event().__class__.__name__)