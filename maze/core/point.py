# -*- coding: utf-8 -*-
#
# point.py
# created by giginet on 2012/11/14
#
import math
class Point (object):
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__ (self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __eq__ (self, p):
        return self.x is p.x and self.y is p.y

    def __mul__ (self, i):
        return Point(self.x * i, self.y * i)

    def distance(self, p):
        return math.hypot(p.x - self.x, p.y - self.y)
    
    def clone(self, p):
        return Point(self.x, self.y)

    @staticmethod
    def up():
        return Point(0, -1)

    @staticmethod
    def left():
        return Point(-1, 0)

    @staticmethod
    def down():
        return Point(0, 1)

    @staticmethod
    def right():
        return Point(1, 0)

    def rotate(self, direction):
        directions = [Point.up, Point.right, Point.down, Point.left]
        index = directions.index(self)
        if direction == Point.right:
            return directions[(index + 1) % 4]
        return directions[(index - 1) % 4]
