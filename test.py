#!/usr/bin/env python
from scrabble.scrabble import Solver


s = Solver(min_len=3)

t = s.solve('bknuybz')


print(t.get_str(', '))



