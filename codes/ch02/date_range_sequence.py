#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: date_range_sequence.py
@time: 2022/11/9 13:25
@project: clean-code-in-python-note
@desc: P45 日期序列
"""
from datetime import timedelta


class DateRangeSequence:
    """An iterable that contains its own iterator object."""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._range = self._create_range()

    def _create_range(self):
        days = []
        current_day = self.start_date
        while current_day < self.end_date:
            days.append(current_day)
            current_day += timedelta(days=1)
        return days

    def __getitem__(self, day_no):
        return self._range[day_no]

    def __len__(self):
        return len(self._range)


if __name__ == '__main__':
    from datetime import date

    s1 = DateRangeSequence(date(2018, 1, 1), date(2018, 1, 5))
    for day in s1:
        print(day)

    print("s1[0] =", s1[0])
