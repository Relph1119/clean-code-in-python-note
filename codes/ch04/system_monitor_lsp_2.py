#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: system_monitor_openclosed1.py
@time: 2022/11/9 15:50
@project: clean-code-in-python-note
@desc: P111 使用里氏替换原则的监视系统
"""
from collections.abc import Mapping


class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return False

    @staticmethod
    def validate_precondition(event_data: dict):
        """Precondition of the contract of this interfact.
        Validate that the ``event_data`` parameter is properly formed.
        """
        if not isinstance(event_data, Mapping):
            raise ValueError(f"{event_data!r} is not a dict")
        for moment in ("before", "after"):
            if moment not in event_data:
                raise ValueError(f"{moment} not in {event_data}")
            if not isinstance(event_data[moment], Mapping):
                raise ValueError(f"event_data[{moment!r}] is not a dict")


class UnknownEvent(Event):
    """A type of event that cannot be identified from its data."""


class LoginEvent(Event):
    """An event repressenting a user that has just entered the system."""

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return event_data["before"].get("session") == 0 and event_data["after"].get("session") == 1


class LogoutEvent(Event):
    """An event representing a user that has just left the system."""

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return event_data["before"].get("session") == 1 and event_data["after"].get("session") == 0


class TransactionEvent(Event):
    """Represents a transaction that has just occurred on the system."""

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return event_data.get("after").get("transaction") is not None


class SystemMonitor:
    """Identify events that occurred in the system."""

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        Event.validate_precondition(self.event_data)
        event_cls = next(
            (event_cls for event_cls in Event.__subclasses__() if event_cls.meets_condition(self.event_data)),
            UnknownEvent)

        return event_cls(self.event_data)


if __name__ == '__main__':
    l1 = SystemMonitor({"before": {"session": 0}, "after": {"session": 1}})
    print("the current event is", l1.identify_event().__class__.__name__)

    l2 = SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
    print("the current event is", l2.identify_event().__class__.__name__)

    l3 = SystemMonitor({"before": {"session": 1}, "after": {"session": 1}})
    print("the current event is", l3.identify_event().__class__.__name__)

    l4 = SystemMonitor({"before": {}, "after": {"transaction": "Tx001"}})
    print("the current event is", l4.identify_event().__class__.__name__)
