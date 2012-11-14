# -*- coding: utf-8 -*-
#
# maze.py
# created by giginet on 2012/11/14
#
from point import Point
class Maze(object):

    def __init__(self, filename):
        f = open(filename)
        self._parse(f.read())

    def _parse(self, string):
        lines = string.split('\n')
        self.width = max(map(lambda l: len(l), lines[0]))
        self.height = len(lines)
        self._map = [[0 for y in xrange(self.height)] for x in xrange(self.width)]
        for y, line in enumerate(lines):
            for x, c in enumerate(line.split()):
                if c == 'S':
                    self._start_position = Point(x, y)
                    self._map[x][y] = 1
                elif c == 'G':
                    self._goal_position = Point(x, y)
                    self._map[x][y] = 1
                elif c == '.':
                    self._map[x][y] = 1

    @property
    def start_position(self):
        return self._start_position

    @property
    def goal_position(self):
        return self._goal_position

    def get_tile(self, position):
        return self._map[position.x][position.y]
