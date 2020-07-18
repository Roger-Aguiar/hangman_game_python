# Name:         Roger Silva Santos Aguiar
# Function:     This is the main module of the application, the hangman game.
# Initial date: July 17, 2020
# Last update:  July 18, 2020

# Required modules
import words_list
import hangman_drawings


class HangmanGame:
    def __init__(self, error):
        self.error = error
        self.letters_of_the_user = []

    def get_word(self):
        run = words_list.Words()
        word = run.choose_word()
        return word

    def guess_letter(self, word_of_the_game):
        word_of_the_player = ""
        attempts = 6

        hangman_drawings.HangmanDrawing.draw_hangman_drawing(0)
        print('Word: ')
        print('__ ' * len(word_of_the_game))

        while len(word_of_the_player) < len(word_of_the_game):
            letter = input('\nEnter a letter: ')

            if letter in word_of_the_game:
                word_of_the_player = self.write_letter_of_the_player(letter, word_of_the_game)
                print("Your word: " + word_of_the_player)
                print("You have {} more attempts." .format(attempts))
            else:
                self.error = self.error + 1
                attempts = attempts - 1
                hangman_drawings.HangmanDrawing.draw_hangman_drawing(self.error)
                print("You have {} more attempts.".format(attempts))
                print("Your word: " + word_of_the_player)
            if self.error > 6:
                hangman_drawings.HangmanDrawing.draw_hangman_drawing(self.error)
                print('You lose!')
                print('Word of the game: ' + word_of_the_game)
                break

        if len(word_of_the_player) == len(word_of_the_game) and self.error <= 6:
            self.display_you_win()

    def write_letter_of_the_player(self, letter, word_of_the_game):
        position_of_the_letter = 0
        word_of_the_player = ''

        while position_of_the_letter < len(word_of_the_game):
            if letter == word_of_the_game[position_of_the_letter]:
                self.letters_of_the_user.insert(position_of_the_letter, letter)

            position_of_the_letter = position_of_the_letter + 1

        for caractere in self.letters_of_the_user:
            word_of_the_player = word_of_the_player + caractere

        return word_of_the_player

    def display_you_win(self):
        winner = """
                    *          *    ********        *               *    *                                       * * *           *   *
                     *        *  *            *     *               *     *                                     *    **          *   *
                      *      * *               *    *               *      *                                   *   * * *         *   *
                       *    * *                 *   *               *       *                                 *    * *  *        *   *
                        *  * *                   *  *               *        *               *               *     * *   *       *   *
                         ** *                     * *               *         *             * *             *      * *    *      *   *
                         ** *                     * *               *          *           *   *           *       * *     *     *   *
                         ** *                     * *               *           *         *     *         *        * *      *    *   *
                         **  *                   *  *               *            *       *       *       *         * *       *   *   *
                         **   *                 *    *             *              *     *         *     *          * *        *  *   *
                         **    *               *      *           *                *   *           *   *           * *         * *   *
                         **     *             *        *         *                  * *             * *            * *          **
                         **        **********            ********                    *               *             * *           *   *
                 """
        print(winner)


if __name__ == '__main__':
    game = HangmanGame(0)
    word_of_the_game = game.get_word()
    print("Word: " + word_of_the_game)

    game.guess_letter(word_of_the_game)
