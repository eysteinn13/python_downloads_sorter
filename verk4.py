#!/usr/bin/env python
import os
import shutil
# from os.path import join as j
def sort(directory, show):
    if not os.path.exists(directory):
        os.makedirs(directory) # add directory
        shutil.rmtree(directory) # remove directory

# returns a list of a few generated search strings
# E.g input = The Big Bang Theory
#       retunrs thebigbangtheory
#               tbbt
#               the.big.bang.theory
#               the-big-bang-theory            
def make_search_strings(str):




sort('shows', 'bla')
