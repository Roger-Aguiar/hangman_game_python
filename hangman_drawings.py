# Name:         Roger Silva Santos Aguiar
# Function:     This module contains  list of the drawing hangman in each time that the user makes a mistake.
# Initial date: July 17, 2020
# Last update:  July 17, 2020

class HangmanDrawing:
    @staticmethod
    def return_hangman_drawing(error):
        hangman_drawings = [
            """
                      ------------------
                      |                |
                      |                |
                      |                |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                -------------
            """,
            """
                      ------------------
                      |                |
                      |                |
                      |                |
                      |                O
                      |
                      |
                      |
                      |
                      |
                      |
                -------------
            """,
            """
                      ------------------
                      |                |
                      |                |
                      |                |
                      |                O
                      |                |
                      |                |
                      |                |
                      |
                      |
                      |
                -------------
            """,
            """
                      ------------------
                      |                |
                      |                |
                      |                |
                      |                O
                      |                |
                      |                |
                      |                |
                      |               *
                      |              *
                      |             *
                -------------
            """,
            """
                      ------------------
                      |                |
                      |                |
                      |                |
                      |                O
                      |                |
                      |                | 
                      |                |  
                      |               * *
                      |              *   *
                      |             *     *
                -------------
            """,
            """
                      ------------------
                      |                |
                      |                |
                      |                |
                      |                O
                      |               *|
                      |             *  | 
                      |           *    |  
                      |               * *
                      |              *   *
                      |             *     *
                -------------
            """,
            """
                      ------------------
                      |                |
                      |                |
                      |                |
                      |                O
                      |               *|*
                      |             *  |  *
                      |           *    |    *
                      |               * *
                      |              *   *
                      |             *     *
                -------------
            """,
            """
                      ------------------
                      |                |
                      |                |              
                      |                O
                      |      ---------------------
                      |               *|*
                      |             *  |  *
                      |           *    |    *
                      |               * *
                      |              *   *
                      |             *     *
                      |
                -------------
            """
        ]

        print(hangman_drawings[error])