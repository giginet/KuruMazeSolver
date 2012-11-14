# -*- coding: utf-8 -*-
#
# state.py
# created by giginet on 2012/11/14
#
from maze.core.point import Point
class State(object):
    def __init__(self, maze, player_position, player_direction):
        self._maze = maze
        self.position = player_position
        self.direction = player_direction

    def is_goal(self):
        return self.position == self.maze.goal_position

    def is_death(self):
        if self.position.x < 0 or self.position.x >= self.maze.width or self.position.y < 0 or self.position.y >= self.maze.height:
            return 0
        return self.get_tile(self.position) == 0

    def next_state(self, rotate_position, rotate_direction):
        x = rotate_position.x
        y = rotate_position.y
        if x >= self.maze.width - 1 or x < 0 or y >= self.maze.height - 1 or y < 0:
            return None
        if not rotate_direction == Point.right or not rotate_direction == Point.left:
            return None
        new_position = self.position.clone()

        # プレイヤーの向きを変える
        new_direction = self.direction.rotate(rotate_direction)
        
        # 回転で移動させる
        if self.position == rotate_position:
            if rotate_direction == Point.left:
                new_position = self.position + Point.down
            elif rotate_direction == Point.right:
                new_position = self.position + Point.right
        elif self.position == rotate_position + Point.right:
            if rotate_direction == Point.left:
                new_position = self.position + Point.left
            elif rotate_direction == Point.right:
                new_position = self.position + Point.down
        elif self.position == rotate_position + Point.right + Point.down:
            if rotate_direction == Point.left:
                new_position = self.position + Point.up
            elif rotate_direction == Point.right:
                new_position = self.position + Point.left
        elif self.position == rotate_position + Point.down:
            if rotate_direction == Point.left:
                new_position = self.position + Point.right
            elif rotate_direction == Point.right:
                new_position = self.position + Point.up

        # 移動させる
        new_position = new_position + new_direction
        state = State(self.maze, new_position, new_direction)
        if state.is_death():
            return None
        return state

    def dump(self):
        dump = ''
        for y in xrange(self.maze.height):
            for x in xrange(self.maze.width):
                p = Point(x, y)
                tile = self.maze.get_tile(p)
                if self.position == p:
                    dump += 'P'
                elif self.maze.goal_position == p:
                    dump += 'G'
                if tile == 1:
                    dump += '.'
                else:
                    dump += ' '
                    dump += '.'
            dump += '\n'
