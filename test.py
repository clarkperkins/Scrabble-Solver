#!/usr/bin/env python
import sys

from scrabble.scrabble import Solver


def main():
    try:
        s = Solver()

        print

        will_continue = 'y'

        while will_continue in ['y', 'Y']:
            letters = raw_input('Enter your letters: ')

            wl = s.solve(letters)

            print

            print wl.sorted_words()

            will_continue = raw_input('Would you like to try again? (Y|N) ')

    except KeyboardInterrupt:
        sys.stdout.flush()
        print 'exiting...'


if __name__ == '__main__':
    main()




