#!/usr/bin/env python
import os
import shutil
import errno
from distutils import dir_util
# from os.path import join as j
def sort(directory, show):
    search_strings = make_search_strings(show)
    if not os.path.exists(directory):
        os.makedirs(directory) # add directory
        # shutil.rmtree(directory) # remove directory
    os.chdir(directory)
    if not os.path.exists(show):
        os.makedirs(show)
    os.chdir('..')

    for root, dirs, files in os.walk("downloads"):
        for f in files:
            if f == '.DS_Store':
                break
            for ST in search_strings:
                if ST in f.lower():
                    shutil.copyfile(os.path.abspath(os.path.join(root, f)), os.path.abspath(os.path.join('shows/'+ show, f)))
                    # shutil.move(os.path.abspath(os.path.join(root, f)), os.path.abspath(os.path.join('shows/'+ show, f)))
                else:
                    if ST in root.lower():
                        # cutta a rettum stad i pathinu
                        ind = root.lower().index(ST)
                        for i in range(root.lower().index(ST), 8, -1):
                            if root[i] == '/':
                                ind = i
                                break
                        ind += 1
                        src = os.path.abspath(root)
                        dest = os.path.abspath(os.path.join('shows/', root[ind:]))
                        if not os.path.exists(dest):
                            dir_util.copy_tree(src, dest)

def sort_folder(folderPath):
    pass

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
    # t = ''.join([i[0] for i in t])
    # l.append(t)
    return l

sort('shows', 'Frasier')
