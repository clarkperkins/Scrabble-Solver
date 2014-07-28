
class WordListNode(object):
    """
    A node within the tree structure.  Not meant to be used on its own
    """

    def __init__(self, char, end, subtree=None):
        assert isinstance(char, basestring)
        assert isinstance(end, bool)

        self._char = char
        self._end = end
        # Subtree of TrieNodes
        if isinstance(subtree, dict):
            self._subtree = subtree
        else:
            self._subtree = {}

    def insert(self, word):
        if len(word) == 0:
            self._end = True
            return
        else:
            next_node = self._subtree.setdefault(word[0], WordListNode(word[0], False))
            next_node.insert(word[1:])

    def is_word(self, word):
        if len(word) == 0:
            return self._end
        else:
            next_node = self._subtree.get(word[0])
            if next_node:
                return next_node.is_word(word[1:])
            else:
                return False

    def is_prefix(self, prefix):
        if len(prefix) == 0:
            return True
        else:
            next_node = self._subtree.get(prefix[0])
            if next_node is not None:
                return next_node.is_prefix(prefix[1:])
            else:
                return False

    def get_words(self, prefix):
        """
        Get a list of words in the sub-Trie
        """
        ret = []
        if self._end:
            ret.append('{0}{1}'.format(str(prefix), str(self._char)))
        for let in sorted(self._subtree):
            ret.extend(self._subtree[let].get_words(prefix+self._char))
        return ret

    def generator(self, prefix):
        """
        Generator for loops - used in Trie
        t = Trie()
        ...
        for word in t:
            do something
        """
        if self._end:
            yield '{0}{1}'.format(str(prefix), str(self._char))
        for let in sorted(self._subtree):
            for word in self._subtree[let].generator(prefix+self._char):
                yield word

    def word_count(self):
        count = 0
        if self._end:
            count += 1
        for subtree in self._subtree.values():
            count += subtree.word_count()
        return count

    def __eq__(self, other):
        if not isinstance(other, WordListNode):
            return False
        if self._char != other._char:
            return False
        if self._end != other._end:
            return False
        if set(self._subtree) != set(other._subtree):
            return False
        for let in self._subtree:
            if not (self._subtree[let] == other._subtree[let]):
                return False
        return True

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self):
        return 'TrieNode({0}, {1}, {2})'.format(
            repr(self._char),
            repr(self._end),
            repr(self._subtree))

    def __str__(self):
        return self.get_words('')


class WordList(object):
    """
    An efficient data structure used for storing a large list of words
    """

    def __init__(self, root=None):
        if isinstance(root, WordListNode):
            self._root = root
        else:
            self._root = WordListNode('', False)

    def insert(self, word):
        """

        :param word:
        :return:
        """
        self._root.insert(word.lower())

    def load_from_file(self, filename):
        """

        :param filename:
        :return:
        """
        with open(filename, 'r') as f:
            for word in f:
                self.insert(word.strip())

    def load_words(self, words):
        """

        :param words:
        :return:
        """
        for word in words:
            self.insert(word)

    def __contains__(self, word):
        return self._root.is_word(word)

    def is_prefix(self, prefix):
        """

        :param prefix:
        :return:
        :rtype: bool
        """
        return self._root.is_prefix(prefix)

    def __len__(self):
        return self._root.word_count()

    def __iter__(self):
        return self._root.generator('')

    def __eq__(self, other):
        return isinstance(other, WordList) and self._root == other.root

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self):
        return 'Trie({0})'.format(repr(self._root))

    def get_str(self, delimiter='\n'):
        """

        :param delimiter:
        :return:
        :rtype: type(delimiter)
        """
        return delimiter.join(self._root.get_words(''))

    def __str__(self):
        return self.get_str()