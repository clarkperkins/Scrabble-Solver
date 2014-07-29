#!/usr/bin/env python
import sys

from scrabble.scrabble import Solver

if __name__ == '__main__':
    try:
        s = Solver()

        letters = raw_input('Enter your letters: ')

        wl = s.solve(letters)

        sorter = {}

        for word in wl:
            sorter.setdefault(len(word), []).append(word)

        print

        for length, words in sorted(sorter.items()):
            print '{0} letter words ({1}):'.format(length, len(words))
            print ', '.join(sorted(words))
            print

    except KeyboardInterrupt:
        sys.stdout.flush()
        print 'exiting...'



