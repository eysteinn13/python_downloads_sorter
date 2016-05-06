#!/usr/bin/env python
import os
import shutil
# from os.path import join as j
def sort(directory, show):
    if not os.path.exists(directory):
        os.makedirs(directory) # add directory
        make_search_strings(show)
        shutil.rmtree(directory) # remove directory

# returns a list of a few generated search strings
# E.g input = The Big Bang Theory
#       returns thebigbangtheory
#               tbbt
#               the.big.bang.theory
#               the-big-bang-theory
def make_search_strings(inp):
    inp = inp.lower()
    l = []
    l.append(inp)
    t = inp.replace(' ', '.')
    l.append(t)
    t = inp.replace(' ', '-')
    l.append(t)
    t = inp.replace(' ', '')
    l.append(t)
    t = inp.split(' ')
    t = ''.join([i[0] for i in t])
    l.append(t)
    return l

sort('shows', 'The Big Bang Theory')
