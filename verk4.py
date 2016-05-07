#!/usr/bin/env python
import os
import shutil
import errno
from distutils import dir_util
import pprint
import re
pp = pprint.PrettyPrinter(indent=4)
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
                if ST in f.lower():# jaja
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
                        dest = os.path.abspath(os.path.join(directory + '/' + show, root[ind:]))
                        if not os.path.exists(dest):
                            dir_util.copy_tree(src, dest)
    sort_folder(directory, show)

def sort_folder(directory, show):
    # Todo: remove duplicate files
    for root, dirs, files in os.walk(directory + '/' + show):
        for d in dirs:
            tempList = []
            for f in files:
                # print f
                season = find_season(os.path.join(d, f))
                print season
                if f in tempList:
                    os.remove(os.path.abspath(os.path.join(root, f)))
                else:
                    tempList.append(f)
    print(len(tempList))

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

def find_season(path):
    # regex
    # s09e02
    # 2x03
    # 02x03
    # -----
    # Season 2
    # S2
    # 403 -> season 4, ep 3

    #p = re.compile('((S|s){1}(\d){2})|((\d){1,2}(x){1}(\d){1,2})|((Season){1})')
    p = re.compile('((S|s){1}(\d){2})')
    if p.search(path) != None:
        found = p.search(path).group()
        found = found[1:]
        if found[0] != 0:
            return int(found)
        else:
            return int(found[1])
    p = re.compile('((\d){1,2}(x){1}(\d){1,2})')


    return -1


# fall til ad removea filea sem enda ekki ekki a avi, mp4, o.fl


sort('shows', 'House of cards')
