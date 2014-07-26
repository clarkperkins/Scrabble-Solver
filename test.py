#!/usr/bin/env python
from scrabble.trie import Trie, TrieNode


t = Trie()

t.load_from_file('test.txt')

for i in t:
    print i
