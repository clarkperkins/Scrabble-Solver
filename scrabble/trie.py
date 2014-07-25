
class TrieNode(object):

    def __init__(self, char, end):
        assert isinstance(char, str)
        assert isinstance(end, bool)

        self.char = char
        self.end = end
        # Subtree of TrieNodes
        self.subtree = {}

    def insert(self, word):
        assert isinstance(word, str)

        if len(word) == 0:
            self.end = True
            return
        else:
            next_node = self.subtree.setdefault(word[0], TrieNode(word[0], False))
            next_node.insert(word[1:])

    def is_word(self, word):
        assert isinstance(word, str)

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

    def print_words(self, prefix, delimiter):
        ret = ''
        if self.end:
            ret += '{0}{1}{2}'.format(prefix, self.char, delimiter)
        for subtree in self.subtree.values():
            ret += subtree.print_words(prefix+self.char, delimiter)
        return ret

    def word_count(self):
        count = 0
        if self.end:
            count += 1
        for subtree in self.subtree.values():
            count += subtree.word_count()
        return count

    def __str__(self):
        return '{0} {1} {2}'.format(self.char, self.end, self.subtree.keys())


class Trie(object):

    def __init__(self):
        self.root = TrieNode('', False)

    def insert(self, word):
        self.root.insert(word.lower())

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                self.insert(line.strip())

    def is_word(self, word):
        return self.root.is_word(word)

    def is_prefix(self, prefix):
        return self.root.is_prefix(prefix)

    def word_count(self):
        return self.root.word_count()

    def get_words(self, delimiter='\n', remove_last=True):
        ret = self.root.print_words('', delimiter)
        return ret[:-len(delimiter)] if remove_last else ret

    def print_words(self, delimiter='\n'):
        print self.get_words(delimiter)

    def __str__(self):
        return self.get_words()