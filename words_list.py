# Name:         Roger Silva Santos Aguiar
# Function:     This module contains a list of words for the hangman game.
# Initial date: July 17, 2020
# Last update:  July 19, 2020

# Required modules
import random

class Words:
    def __init__(self):
        self.words = ['aback', 'abacus', 'abalone', 'abandon', 'abandoned', 'abandonment', 'abase', 'abashed',
                      'abate', 'abatoir', 'abaya', 'abba', 'abbess', 'abbey', 'abbot', 'abbreviate', 'abbreviation',
                      'abdicate', 'abdomen', 'abdominal', 'abduct', 'abductee' 'abductor', 'abed', 'aberrant',
                      'aberration', 'abet', 'abhor', 'abhorrence']

    def choose_word(self):
        return random.choice(self.words)

