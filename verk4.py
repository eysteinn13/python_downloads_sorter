#!/usr/bin/env python
import os
import shutil
# from os.path import join as j
def sort(directory, show):
    if not os.path.exists(directory):
        os.makedirs(directory) # add directory
        shutil.rmtree(directory) # remove directory

sort('shows', 'bla')
