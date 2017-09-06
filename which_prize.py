#!/usr/bin/env python
"""Program: Which Prize
Programmer: Michael Fryar
Created: 2017.08.20
Purpose: Practice conditional statements and booleans
"""


def which_prize(points):
    """Returns the prize-winning message, given a number of points"""
    prize = None
    if points <= 50:
        prize = "wooden rabbit"
    elif 150 < points <= 180:
        prize = "wafer-thin mint"
    elif 180 < points <= 200:
        prize = "penguin"
    if prize:
        return "Congratulations! You have won a {}!".format(prize)
    else:
        return "Oh dear, no prize this time."
which_prize(12)
which_prize(149)
which_prize(164)
which_prize(194)
