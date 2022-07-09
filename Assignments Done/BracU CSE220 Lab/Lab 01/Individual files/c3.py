#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
__author__ = "Muntasir Rahman Eram"
__title__ = "FALL21 CSE220 Lab 1 - Array Tasks"


# Helper function to move players clockwise for
# each generated random number that isn't 1.
def one_turn_clockwise(players):
    new=[]
    for i in range(1, len(players)):
        new.append(players[i])
    new.append(players[0])
    for i in range(0, len(players)):
        players[i] = new[i]

def one_round(players):
    flag_playerNotleft = False
    num = random.randint(0,3)  # a random number between 0 to 3 inclusive.
    if num != 1:
        one_turn_clockwise(players) # Turn once if num is not 1
    else:
        if len(players) == 1:
            print(f"{players[0]} wins!!!")  # Only remaining player must be at 0 idx.
            flag_playerNotleft = True
        else:
            # If more than 1 player is left, player(n/2) gets eliminated.
            rem_idx = int(len(players)/2)
            print(f"Eliminating {players[rem_idx]}")
            players.remove(players[rem_idx])
            print(f"Remaining players are - {players}")
    if flag_playerNotleft:
        return "end"
    else:
        return "not end"


if __name__ == '__main__':
    players = ["player 1", "player 2", "player 3", "player 4",
              "player 5", "player 6", "player 7"]

    while one_round(players)!= "end":
        one_round(players)
