from datetime import datetime
import sys

from .wordlist import WordList


class Solver(object):
    """

    """
    DEFAULT_MIN_LEN = 2

    letter_mapping = dict(
        a=1, b=4, c=4, d=2, e=1, f=4, g=3, h=3, i=1, j=10, k=5, l=2, m=4,
        n=2, o=1, p=4, q=10, r=1, s=1, t=1, u=2, v=5, w=4, x=8, y=3, z=10,
    )

    def __init__(self, min_len=DEFAULT_MIN_LEN, dict_file='scrabble/dictionaries/ospd.txt'):
        self._dict = WordList()
        print 'Loading legal word list...',
        sys.stdout.flush()
        self._dict.load_from_file(dict_file)
        print 'Done!'

        self._min_len = min_len
        self._tmp_wordlist = None

    def _solve_help(self, remaining, pre):
        if len(pre) >= self._min_len and pre in self._dict:
            self._tmp_wordlist.insert(pre)

        if not self._dict.is_prefix(pre):
            return

        for let in remaining:
            if let == '?':
                r = remaining.replace(let, '', 1)
                for sublet in self.letter_mapping:
                    self._solve_help(r, pre+sublet)
            else:
                self._solve_help(remaining.replace(let, '', 1), pre+let)

    def solve(self, string):
        """

        :param string: the cluster of letters to scramble
        :return: A WordList containing the found words
        :rtype: WordList
        """
        print 'Solving...',
        sys.stdout.flush()
        start = datetime.now()
        # Create a new wordlist
        self._tmp_wordlist = WordList()
        self._solve_help(string.lower(), '')
        diff = datetime.now() - start

        num_words = len(self._tmp_wordlist)
        print 'Done!'
        print 'Found {0} word{1} in {2} seconds.'.format(
            num_words,
            '' if num_words == 1 else 's',
            diff.microseconds * (10 ** -6)
        )

        # Don't hold on to the reference
        tmp = self._tmp_wordlist
        self._tmp_wordlist = None
        return tmp

    def _match_help(self, remaining, pre):
        if len(remaining) == 0:
            if pre in self._dict:
                self._tmp_wordlist.insert(pre)
            return

        if not self._dict.is_prefix(pre):
            return

        if remaining[0] == '?':
            for sublet in self.letter_mapping:
                if len(remaining) <= 1:
                    self._match_help('', pre+sublet)
                else:
                    self._match_help(remaining[1:], pre+sublet)
        else:
            if len(remaining) <= 1:
                self._match_help('', pre+remaining[0])
            else:
                self._match_help(remaining[1:], pre+remaining[0])

    def match(self, match_str):
        """

        :param match_str:
        :return: A WordList containing matching words
        :rtype: WordList
        """
        print 'Matching...',
        sys.stdout.flush()
        start = datetime.now()

        self._tmp_wordlist = WordList()
        self._match_help(match_str, '')

        diff = datetime.now() - start

        num_words = len(self._tmp_wordlist)
        print 'Done!'
        print 'Matched {0} word{1} in {2} seconds.'.format(
            num_words,
            '' if num_words == 1 else 's',
            diff.microseconds * (10 ** -6)
        )

        # Don't hold on to the reference
        tmp = self._tmp_wordlist
        self._tmp_wordlist = None
        return tmp


