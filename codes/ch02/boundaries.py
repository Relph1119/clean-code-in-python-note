#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: boundaries.py
@time: 2022/11/9 13:34
@project: clean-code-in-python-note
@desc: P46 容器对象-地图
"""


class Boundaries:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __contains__(self, coord):
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.limits = Boundaries(width, height)
        self._grid = [[0 for _ in range(height)] for _ in range(width)]

    def __contains__(self, coord):
        return coord in self.limits

    def __setitem__(self, key, value):
        self._grid[key[0]][key[1]] = value

    def __str__(self):
        return self._grid.__str__()


MARKED = 1


def make_coordinate(grid, coord):
    if coord in grid:
        grid[coord] = MARKED


if __name__ == '__main__':
    grid = Grid(3, 4)
    make_coordinate(grid, (2, 3))
    print(grid)
