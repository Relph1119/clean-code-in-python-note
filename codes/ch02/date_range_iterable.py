#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: date_range_iterable.py
@time: 2022/11/9 12:47
@project: clean-code-in-python-note
@desc: P42 创建可迭代对象，日期迭代器
"""
from datetime import timedelta


class DateRangeIterable:
    """An iterable that contains its own iterator object."""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today

    class DateRangeContainerIterable:
        def __init__(self, start_date, end_date):
            self.start_date = start_date
            self.end_date = end_date


if __name__ == '__main__':
    from datetime import date

    r1 = DateRangeIterable(date(2018, 1, 1), date(2018, 1, 5))
    for day in r1:
        print(day)

    print(", ".join(map(str, r1)))
    print(max(r1))
