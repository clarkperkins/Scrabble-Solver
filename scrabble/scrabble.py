from datetime import datetime
import sys

from .wordlist import WordList


class Solver(object):
    """

    """
    DEFAULT_MIN_LEN = 3

    letter_mapping = dict(
        a=1, b=4, c=4, d=2, e=1, f=4, g=3, h=3, i=1, j=10, k=5, l=2, m=4,
        n=2, o=1, p=4, q=10, r=1, s=1, t=1, u=2, v=5, w=4, x=8, y=3, z=10,
    )

    def __init__(self, min_len=DEFAULT_MIN_LEN, dict_file='scrabble/dictionaries/ospd.txt'):
        self._dict = WordList()
        print('Loading legal word list...'),
        sys.stdout.flush()
        self._dict.load_from_file(dict_file)
        print('Done!')

        self._min_len = min_len
        self._tmp_trie = None

    def _solve_help(self, remaining, pre):
        if len(pre) >= self._min_len and pre in self._dict:
            self._tmp_trie.insert(pre)

        if not self._dict.is_prefix(pre):
            return

        for let in remaining:
            self._solve_help(remaining.replace(let, '', 1), pre+let)

    def solve(self, string):
        """

        :param string: the cluster of letters to scramble
        :return: A WordList containing the found words
        :rtype: WordList
        """
        print('Solving...'),
        sys.stdout.flush()
        start = datetime.now()
        # Create a new trie
        self._tmp_trie = WordList()
        self._solve_help(string, '')
        diff = datetime.now() - start

        num_words = len(self._tmp_trie)
        print('Done!')
        print('Found {0} word{1} in {2} seconds.'.format(
            num_words,
            '' if num_words == 1 else 's',
            diff.seconds
        ))

        # Don't hold on to the reference
        tmp = self._tmp_trie
        self._tmp_trie = None
        return tmp

    def running(self):
        """

        :return:
        :rtype: bool
        """
        return self._tmp_trie is not None