#!/usr/bin/env python
import os
import shutil
from distutils import dir_util
import sys
import re

def sort(directory, show):
    search_strings = make_search_strings(show)
    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.exists('All music'):
        os.makedirs('All Music')
    if not os.path.exists('All Images'):
        os.makedirs('All Images')
    os.chdir(directory)
    if not os.path.exists(show):
        os.makedirs(show)
    os.chdir('..')
    # change downloads to the dir you want to sort, maybe send this in as a param, or use current directory?
    for root, dirs, files in os.walk("downloads"):
        for f in files:
            if f.endswith('.mp3'):
                shutil.move(os.path.abspath(os.path.join(root, f)), os.path.abspath(os.path.join('All Music/', f)))
                continue
            if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg') or f.endswith('.svg') or f.endswith('.gif'):
                shutil.move(os.path.abspath(os.path.join(root, f)), os.path.abspath(os.path.join('All Images/', f)))
                continue
            rar_pattern = re.compile('(\.){1}(r){1}(\d){2}$')
            if f.endswith('.txt') or f.endswith('.nfo') or f.endswith('.rar') or rar_pattern.search(f) != None:
                os.remove(os.path.abspath(os.path.join(root, f)))
                continue
            if f == '.DS_Store':
                continue
            for ST in search_strings:
                if ST in f.lower():
                    shutil.move(os.path.abspath(os.path.join(root, f)), os.path.abspath(os.path.join(directory + '/'+ show, f)))
                    break
                else:
                    if ST in root.lower():
                        # cut in the right place in the path
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
                        os.remove(os.path.abspath(os.path.join(root,f)))
                        break
    remove_empty_folders('.')
    sort_folder(directory, show)

def sort_folder(directory, show):
    for root, dirs, files in os.walk(directory + '/' + show):
        for f in files:
            if f == '.DS_Store':
                continue
            season = find_season(os.path.join(root, f))
            if season: # move file to the correct folder
                season = str(season)
                if not os.path.exists(directory + '/' + show + '/Season ' + season):
                    os.makedirs(directory + '/' + show + '/Season ' + season)
                src = os.path.abspath(os.path.join(root, f))
                dst = os.path.abspath(directory + '/' + show + '/Season ' + season)
                if not os.path.exists(directory + '/' + show + '/Season ' + season + '/' + f):
                    shutil.move(src,dst)
                else :
                    if os.path.abspath(directory + '/' + show + '/Season ' + season + '/' + f) != os.path.abspath(os.path.join(root, f)):
                        os.remove(os.path.abspath(os.path.join(root,f)))
            else :
                src = os.path.abspath(os.path.join(root, f))
                dst = os.path.abspath(directory + '/' + show)
                if not os.path.exists(directory + '/' + show + '/' + f):
                    shutil.move(src,dst)
                    print 'hehe'
                else :
                    if os.path.abspath(directory + '/' + show + '/' + f) != os.path.abspath(os.path.join(root, f)):
                        os.remove(os.path.abspath(os.path.join(root,f)))
    # clear empty folders
    remove_path = os.path.abspath(directory + '/' + show)
    remove_empty_folders(remove_path)

def make_search_strings(inp):
    inp = inp.lower()
    search_strings = []
    search_strings.append(inp)
    t = inp.replace(' ', '.')
    search_strings.append(t)
    t = inp.replace(' ', '-')
    search_strings.append(t)
    t = inp.replace(' ', '')
    search_strings.append(t)
    return search_strings

def find_season(path):
    # S02 | S2
    p = re.compile('((S|s){1}(\d){1,2})')
    if p.search(path) != None:
        found = p.search(path).group()
        found = found[1:]
        if found[0] == '0':
            return int(found[1])
        else:
            return int(found)

    # 1x03 | 01x03
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

    # Season 2
    p = re.compile('Season{1}(.){1}(\d){1,2}')
    if p.search(path) != None:
        found = p.search(path).group()
        found = found[-2:]
        if found[0].isdigit() and found[0] != '0':
            return int(found)
        else:
            return int(found[1])

    return False

# Got this from GitHub - Jacob Tom Linson: https://gist.github.com/jacobtomlinson/9031697
def remove_empty_folders(path, removeRoot=True):
  if not os.path.isdir(path):
    return
  # remove empty subfolders
  files = os.listdir(path)
  if len(files):
    for f in files:
      fullpath = os.path.join(path, f)
      if os.path.isdir(fullpath):
        remove_empty_folders(fullpath)

  # if folder empty, delete it
  files = os.listdir(path)
  if len(files) == 0 and removeRoot:
    os.rmdir(path)

sort(sys.argv[1], sys.argv[2])
