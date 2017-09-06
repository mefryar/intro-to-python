#!/usr/bin/env python
"""Program: Which Prize
Programmer: Michael Fryar
Created: 2017.08.20
Purpose: Practice conditional statements
"""


def which_prize(points):
    """Returns the prize-winning message, given a number of points"""
    if points <= 50:
        prize_name = "wooden rabbit"
    elif 150 < points <= 180:
        prize_name = "wafer-thin mint"
    elif 180 < points <= 200:
        prize_name = "penguin"
    else:
        prize_name = "No prize"
    if 50 < points <= 150:
        message = "Oh dear, no prize this time."
    else:
        message = "Congratulations! You have won a {}!".format(prize_name)
    print(message)
which_prize(50)
which_prize(51)
which_prize(180)
which_prize(181)
