
class TrieNode(object):
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
            next_node = self._subtree.setdefault(word[0], TrieNode(word[0], False))
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

    def get_words(self, prefix, delimiter='\n'):
        ret = ''
        if self._end:
            ret += '{0}{1}{2}'.format(prefix, self._char, delimiter)
        for let in sorted(self._subtree):
            ret += self._subtree[let].get_words(prefix+self._char, delimiter)
        return ret

    def word_count(self):
        count = 0
        if self._end:
            count += 1
        for subtree in self._subtree.values():
            count += subtree.word_count()
        return count

    def __eq__(self, other):
        if not isinstance(other, TrieNode):
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


class Trie(object):
    """
    A data structure used for storing a dictionary of words
    """

    def __init__(self, root=None):
        if isinstance(root, TrieNode):
            self._root = root
        else:
            self._root = TrieNode('', False)

    def insert(self, word):
        self._root.insert(word.lower())

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            for word in f:
                self.insert(word.strip())

    def load_words(self, words):
        for word in words:
            self.insert(word)

    def is_word(self, word):
        return self._root.is_word(word)

    def is_prefix(self, prefix):
        return self._root.is_prefix(prefix)

    def word_count(self):
        return self._root.word_count()

    def get_words(self, delimiter='\n', remove_last=True):
        ret = self._root.get_words('', delimiter)
        return ret[:-len(delimiter)] if remove_last else ret

    def print_words(self, delimiter='\n'):
        print self.get_words(delimiter)

    def __eq__(self, other):
        return isinstance(other, Trie) and self._root == other.root

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self):
        return 'Trie({0})'.format(repr(self._root))

    def __str__(self):
        return self.get_words()