#!/usr/bin/env python
from scrabble.scrabble import Solver


s = Solver(min_len=3)

wl = s.solve('bknuybz')


print(wl.get_str(', '))



