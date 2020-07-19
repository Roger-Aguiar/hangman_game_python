# Name:         Roger Silva Santos Aguiar
# Function:     This is the main module of the application, the hangman game.
# Initial date: July 17, 2020
# Last update:  July 19, 2020

# Required modules
import words_list
import hangman_drawings


class HangmanGame:
    def __init__(self, error):
        self.error = error
        self.letters_of_the_user = []
        self.word_of_the_player = ''

    def get_word(self):
        run = words_list.Words()
        word = run.choose_word()
        return word

    def guess_letter(self, word_of_the_game):
        word_of_the_player = ""
        count_word_of_the_player = 0
        attempts = 6

        hangman_drawings.HangmanDrawing.draw_hangman_drawing(0)
        print('Word: ')
        print('__ ' * len(word_of_the_game))

        while count_word_of_the_player < len(word_of_the_game):
            letter = input('\nEnter a letter: ')

            if letter in word_of_the_game:
                count_word_of_the_player = self.write_letter_of_the_player(letter, word_of_the_game)
                print("Your word: " + self.word_of_the_player)
                print("You have {} more attempts." .format(attempts))
            else:
                self.error = self.error + 1
                attempts = attempts - 1

                if attempts > -1:
                    hangman_drawings.HangmanDrawing.draw_hangman_drawing(self.error)
                    print("You have {} more attempts.".format(attempts))
                    print("Your word: " + self.word_of_the_player)
            if self.error > 6:
                hangman_drawings.HangmanDrawing.draw_hangman_drawing(self.error)
                self.display_you_lose()
                print('Word of the game: ' + word_of_the_game)
                break

        if count_word_of_the_player == len(word_of_the_game) and self.error <= 6:
            self.display_you_win()

    def write_letter_of_the_player(self, letter, word_of_the_game):
        count_word_of_the_player = 0
        word_index = 0
        self.letters_of_the_user.append(letter)
        self.word_of_the_player = ''

        while word_index < len(word_of_the_game):
            if word_of_the_game[word_index] in self.letters_of_the_user:
                self.word_of_the_player = self.word_of_the_player + word_of_the_game[word_index]
                count_word_of_the_player += 1
            else:
                self.word_of_the_player = self.word_of_the_player + '__ '

            word_index += 1

        return count_word_of_the_player

    def display_you_win(self):
        message = """
                    *           *    ********        *               *    *                                       * * *           *   *
                     *         *  *            *     *               *     *                                     *    **          *   *
                      *       * *               *    *               *      *                                   *   * * *         *   *
                       *     * *                 *   *               *       *                                 *    * *  *        *   *
                        *   * *                   *  *               *        *               *               *     * *   *       *   *
                         * * *                     * *               *         *             * *             *      * *    *      *   *
                          *  *                     * *               *          *           *   *           *       * *     *     *   *
                          *  *                     * *               *           *         *     *         *        * *      *    *   *
                          *   *                   *  *               *            *       *       *       *         * *       *   *   *
                          *    *                 *    *             *              *     *         *     *          * *        *  *   *
                          *     *               *      *           *                *   *           *   *           * *         * *   *
                          *      *             *        *         *                  * *             * *            * *          **
                          *        **********            ********                     *               *             * *           *   *
                 """
        print(message)

    def display_you_lose(self):
        message = """
                    *           *    ********        *               *    *                  ********         **********  ***********   * 
                     *         *  *            *     *               *    *                *          *     *             *             *
                      *       * *               *    *               *    *               *            *   *              *             *
                       *     * *                 *   *               *    *              *              *  *              *             *       
                        *   * *                   *  *               *    *             *                *  *             *             *
                         * * *                     * *               *    *            *                  *  *******      *             *
                          *  *                     * *               *    *            *                  *          *    ***********   *
                          *  *                     * *               *    *            *                  *            *  *             *
                          *   *                   *  *               *    *             *                *              * *             *
                          *    *                 *    *             *     *              *              *               * *             *
                          *     *               *      *           *      *               *            *               *  *             *
                          *      *             *        *         *       *                *          *               *   *             
                          *        **********            ********         * ************     ********        **********   ***********   *
                              
                  """
        print(message)
