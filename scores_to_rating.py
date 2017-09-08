#!/usr/bin/env python

"""Program: scores_to_rating.py
Programmer: Michael Fryar
Date created: September 9, 2017

Purpose: Written for Udacity's Intro to Python Programmming Course
"""


def convert_to_numeric(score):
    """Convert score to float"""
    return float(score)


def sum_of_middle_three(list_of_scores):
    """Return sum of five integers minus minimum and maximum"""
    return sum(list_of_scores) - min(list_of_scores) - max(list_of_scores)


def score_to_rating_string(average_score):
    """Convert numeric rating to string rating"""
    if 0 <= average_score < 1:
        rating = "Terrible"
    elif 1 <= average_score < 2:
        rating = "Bad"
    elif 2 <= average_score < 3:
        rating = "OK"
    elif 3 <= average_score < 4:
        rating = "Good"
    elif 4 <= average_score <= 5:
        rating = "Excellent"
    else:
        rating = "Rating outside of 0 - 5 range"
    return rating


def scores_to_rating(score1, score2, score3, score4, score5):
    """Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    # STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    # STEP 2 store numeric scores in list
    list_of_scores = [score1, score2, score3, score4, score5]

    # STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(list_of_scores)/3

    # STEP 4 turn average score into a rating
    return score_to_rating_string(average_score)
