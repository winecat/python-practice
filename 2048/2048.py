#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import curses
from random import randrange, choice
from collections import defaultdict

letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
actions_dict = dict(zip(letter_codes, actions * 2))

def get_user_action(keyboard):
    char = "N"
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]

def transpose(field):
    return [list(row) for row in zip(*field)]

def invert(field):
    return [row[::-1] for row in field]

class GameField(object):
    def __init(self, height = 4, width = 4, win = 2048):
        self.height = height
        self.width = width
        self.win_value = 2048
        self.score = 0
        self.heigscore = 0
        self.reset()

    def reset(self):
        if self.score > self.heigscore:
            self.heigscore = self.score
        self.score = 0
        self.field = [[0 form i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()
    def move(self, direction):
        
        
 