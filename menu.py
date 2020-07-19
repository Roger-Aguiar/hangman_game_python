# Name:         Roger Silva Santos Aguiar
# Function:     This module is the menu, where the user will run the game and stop the game.
# Initial date: July 19, 2020
# Last update:  July 19, 2020

# Required modules
import hangman_game

class Menu:
    def menu(self):
        print('**************************************************************************Hangman game***************************************************************************\n')
        print('1 - New game')
        print('2 - Exit')
        print('\n***************************************************************************************************************************************************************')


if __name__ == '__main__':
    begin_game = Menu()
    begin_game.menu()

    option = int(input('Choose an option: '))

    while option == 1:
        new_game = hangman_game.HangmanGame(0)
        word_of_the_game = new_game.get_word()
        new_game.guess_letter(word_of_the_game)
        begin_game.menu()
        option = int(input('Choose an option: '))

        if option == 2:
            print("Game over!")