#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: purchases_stats.py
@time: 2022/11/10 14:23
@project: clean-code-in-python-note
@desc: P191 生成器、迭代器的使用
"""
import itertools
from statistics import median


class PurchasesStats:
    def __init__(self, purchases):
        self.purchases = iter(purchases)
        self.min_price: float = None
        self.max_price: float = None
        self._total_purchases_price: float = 0.0
        self._total_purchases = 0
        self._initialize()

    def _initialize(self):
        try:
            first_value = next(self.purchases)
        except StopIteration:
            raise ValueError("no values provided")

        self.min_price = self.max_price = first_value
        self._update_avg(first_value)

    def process(self):
        for purchase_value in self.purchases:
            self._update_min(purchase_value)
            self._update_max(purchase_value)
            self._update_avg(purchase_value)

        return self

    def _update_min(self, new_value: float):
        if new_value < self.min_price:
            self.min_price = new_value

    def _update_max(self, new_value: float):
        if new_value > self.max_price:
            self.max_price = new_value

    @property
    def avg_price(self):
        return self._total_purchases_price / self._total_purchases

    def _update_avg(self, new_value):
        self._total_purchases_price += new_value
        self._total_purchases += 1

    def __str__(self):
        return (
            f"{self.__class__.__name__}({self.min_price}, "
            f"{self.max_price}, {self.avg_price})"
        )


def load_purchases(filename):
    with open(filename) as f:
        for line in f:
            *_, price_raw = line.partition(",")
            # 使用迭代器解决文件内容加载问题
            yield float(price_raw)


def process_purchases(purchases):
    # 使用itertools.tee从原始可迭代对象分裂出3个新的可迭代对象
    min_, max_, avg = itertools.tee(purchases, 3)
    return min(min_), max(max_), median(avg)


if __name__ == '__main__':
    purchases = load_purchases("purchase_data.csv")
    ps = PurchasesStats(purchases)
    ps = ps.process()
    print(ps)

    purchases = load_purchases("purchase_data.csv")
    print(process_purchases(purchases))
