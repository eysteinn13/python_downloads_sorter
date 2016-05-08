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
    for root, dirs, files in os.walk(directory + '/' + show):
        for f in files:
            if f == '.DS_Store':
                continue
            print f
            season = find_season(os.path.join(root, f))
            if season: # move file to the correct folder
                season = str(season)
                if not os.path.exists(directory + '/' + show + '/Season ' + season):
                    os.makedirs(directory + '/' + show + '/Season ' + season)
                src = os.path.abspath(os.path.join(root, f))
                dst = os.path.abspath(directory + '/' + show + '/Season ' + season)
                if not os.path.exists(directory + '/' + show + '/Season ' + season + '/' + f):
                    shutil.move(src,dst)
            # if season could not be determined leave the file.
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
    # REGEX
    # s09e02 - komid
    # 2x03 - komid
    # 02x03 - komid
    # Season 2 - komid
    # S2 - komid
    # -----
    # 403 -> season 4, ep 3 - gera tetta? meikar eiginlega ekki sens

    p = re.compile('((S|s){1}(\d){2})')
    if p.search(path) != None:
        found = p.search(path).group()
        found = found[1:]
        if found[0] != 0:
            return int(found)
        else:
            return int(found[1])

    p = re.compile('((\d){1,2}(x){1}(\d){1,2})')
    if p.search(path) != None:
        found = p.search(path).group()
        found = found.lower()
        index = found.index('x')
        if index == 2:
            if found[0] == '0':
                return int(found[1])
            else:
                return int(found[0:2])
        elif index == 1:
            return int(found[0])

    p = re.compile('(Season){1}(.)*(\d){1,2}')
    if p.search(path) != None:
        found = p.search(path).group()
        found = found[-2:]
        if found[0].isdigit() and found[0] != '0':
            return int(found)
        else:
            return int(found[1])

    p = re.compile('(S){1}(\d){1,2}')
    if p.search(path) != None:
        found = p.search(path).group()
        found = found[1:]
        if found[0] == '0':
            return int(found[1])
        else:
            return int(found)

    return False

# fall til ad removea filea sem enda ekki ekki a avi, mp4, o.fl


sort('shows', 'That \'70s show')
