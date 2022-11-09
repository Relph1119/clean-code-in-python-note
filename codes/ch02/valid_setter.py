#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: valid_setter.py
@time: 2022/11/9 11:18
@project: clean-code-in-python-note
@desc: P36 验证经纬度
"""


class Coordinate:
    def __init__(self, lat: float, long: float) -> None:
        self._latitude = self._longitude = None
        self.latitude = lat
        self.longitude = long

    @property
    def latitude(self) -> float:
        return self._latitude

    @latitude.setter
    def latitude(self, lat_value: float) -> None:
        if lat_value not in range(-90, 90 + 1):
            raise ValueError(f"{lat_value} is an invalid value for lattitude")
        self._latitude = lat_value

    @property
    def longitude(self) -> float:
        return self._longitude

    @longitude.setter
    def longitude(self, long_value: float) -> None:
        if long_value not in range(-180, 180 + 1):
            raise ValueError(f"{long_value} is an invalid value for longitude")
        self._longitude = long_value


if __name__ == '__main__':
    # if latitude is 91, report value error
    coord = Coordinate(90, 129)
    print("the latitude of Coordinate:", coord.latitude)
    print("the longitude of Coordinate:", coord.longitude)
