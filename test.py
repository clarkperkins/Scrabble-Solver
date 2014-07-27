#!/usr/bin/env python
from scrabble.scrabble import Solver


s = Solver(min_len=6)

t = s.solve('smagbet')


print(t.get_str(', '))



