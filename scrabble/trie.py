
class TrieNode(object):

    def __init__(self, char, end, subtree=None):
        assert isinstance(char, basestring)
        assert isinstance(end, bool)

        self.char = char
        self.end = end
        # Subtree of TrieNodes
        if isinstance(subtree, dict):
            self.subtree = subtree
        else:
            self.subtree = {}

    def insert(self, word):
        assert isinstance(word, basestring)

        if len(word) == 0:
            self.end = True
            return
        else:
            next_node = self.subtree.setdefault(word[0], TrieNode(word[0], False))
            next_node.insert(word[1:])

    def is_word(self, word):
        assert isinstance(word, basestring)

        if len(word) == 0:
            return self.end
        else:
            next_node = self.subtree.get(word[0])
            if next_node:
                return next_node.is_word(word[1:])
            else:
                return False

    def is_prefix(self, prefix):
        assert isinstance(prefix, str)

        if len(prefix) == 0:
            return True
        else:
            next_node = self.subtree.get(prefix[0])
            if next_node is not None:
                return next_node.is_prefix(prefix[1:])
            else:
                return False

    def get_words(self, prefix, delimiter='\n'):
        ret = ''
        if self.end:
            ret += '{0}{1}{2}'.format(prefix, self.char, delimiter)
        for let in sorted(self.subtree):
            ret += self.subtree[let].get_words(prefix+self.char, delimiter)
        return ret

    def word_count(self):
        count = 0
        if self.end:
            count += 1
        for subtree in self.subtree.values():
            count += subtree.word_count()
        return count

    def __eq__(self, other):
        if not isinstance(other, TrieNode):
            return False
        if self.char != other.char:
            return False
        if self.end != other.end:
            return False
        if set(self.subtree) != set(other.subtree):
            return False
        for let in self.subtree:
            if not (self.subtree[let] == other.subtree[let]):
                return False
        return True

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self):
        return 'TrieNode({0}, {1}, {2})'.format(
            repr(self.char),
            repr(self.end),
            repr(self.subtree))

    def __str__(self):
        return self.get_words('')


class Trie(object):

    def __init__(self, root=None):
        if isinstance(root, TrieNode):
            self.root = root
        else:
            self.root = TrieNode('', False)

    def insert(self, word):
        self.root.insert(word.lower())

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            for word in f:
                self.insert(word.strip())

    def load_words(self, words):
        for word in words:
            self.insert(word)

    def is_word(self, word):
        return self.root.is_word(word)

    def is_prefix(self, prefix):
        return self.root.is_prefix(prefix)

    def word_count(self):
        return self.root.word_count()

    def get_words(self, delimiter='\n', remove_last=True, sort_length=False):
        ret = self.root.get_words('', delimiter)
        return ret[:-len(delimiter)] if remove_last else ret

    def print_words(self, delimiter='\n'):
        print self.get_words(delimiter)

    def __eq__(self, other):
        return isinstance(other, Trie) and self.root == other.root

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self):
        return 'Trie({0})'.format(repr(self.root))

    def __str__(self):
        return self.get_words()