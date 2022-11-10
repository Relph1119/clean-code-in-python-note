#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: login_event_serializer.py
@time: 2022/11/9 16:54
@project: clean-code-in-python-note
@desc: P127 类装饰器
"""

from dataclasses import dataclass
from datetime import datetime


def hide_field(field) -> str:
    return "**redacted**"


def format_time(field_timestamp: datetime) -> str:
    return field_timestamp.strftime("%Y-%m-%d %H:%M")


def show_original(event_field):
    return event_field


class EventSerializer:
    def __init__(self, serialization_fields: dict) -> None:
        self.serialization_fields = serialization_fields

    def serialize(self, event) -> dict:
        return {
            field: transformation(getattr(event, field)) for field, transformation in self.serialization_fields.items()
        }


class Serialization:
    def __init__(self, **transformations):
        self.serializer = EventSerializer(transformations)

    def __call__(self, event_class):
        def serialize_method(event_instance):
            return self.serializer.serialize(event_instance)

        event_class.serialize = serialize_method
        return event_class


@Serialization(
    username=str.lower,
    password=hide_field,
    ip=show_original,
    timestamp=format_time
)
@dataclass
class LoginEvent:
    username: str
    password: str
    ip: str
    timestamp: datetime


if __name__ == '__main__':
    l1 = LoginEvent("XiaoMing", "123456", "10.100.123.123", datetime(2008, 11, 10))
    print(l1.serialize())
