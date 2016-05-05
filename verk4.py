#!/usr/bin/env python
# from os import walk as w
import os
import shutil
# from os.path import join as j
def sort(directory, show, search_string):
    if not os.path.exists(directory):
        os.makedirs(directory) # add directory
        shutil.rmtree(directory) # remove directory

sort('shows', 'bla', 'bla')
