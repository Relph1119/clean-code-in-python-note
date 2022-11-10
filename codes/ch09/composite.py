#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: composite.py
@time: 2022/11/10 19:43
@project: clean-code-in-python-note
@desc: P269 组合模式
有一个简化版的在线商店，其中有商品，假设这个商店可能将商品编组，并给成组的商品打折。
每件商品都有价格，顾客付款时可直接查询。但对于成组的商品，价格需要通过计算来得到。
"""
from typing import Iterable, Union


class Product:
    def __init__(self, name: str, price: float) -> None:
        self._name = name
        self._price = price

    @property
    def price(self):
        return self._price

class ProductBundle:
    def __init__(self,
                 name:str,
                 perc_discount: float,
                 *products: Iterable[Union[Product, "ProductBundle"]]) -> None:
        self._name = name
        self._perc_discount = perc_discount
        self._products = products

    @property
    def price(self) -> float:
        total = sum(p.price for p in self._products)
        return total * (1 - self._perc_discount)
