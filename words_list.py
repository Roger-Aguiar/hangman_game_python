# Name:         Roger Silva Santos Aguiar
# Function:     This module contains a list of words for the hangman game.
# Initial date: July 17, 2020
# Last update:  July 17, 2020

# Required modules
import random

class Words:
    def __init__(self):
        self.words = ["pheasant", "duck", "turkey", "chicken", "vulture", "full",
                      "albatross", "puffin", "lion", "horn", "beaver", "koala", "kangaroo"]

    def choose_word(self):
        return random.choice(self.words)

