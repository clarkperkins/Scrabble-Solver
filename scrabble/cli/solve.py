from cliff.command import Command


class Solve(Command):
    """
    scrabble solver
    """

    def take_action(self, parsed_args):
        print parsed_args

        # wl = s.solve(letters)
        #
        # print
        #
        # print wl.sorted_words()
        #
        # will_continue = raw_input('Would you like to try again? (Y|N) ')