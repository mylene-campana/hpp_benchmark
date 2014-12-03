#!/usr/bin/env python

import os
from commands import getstatusoutput

DEVEL_DIR=os.getenv ("DEVEL_DIR")

# String formated with package name and file name
git_blame = "cd " + DEVEL_DIR + "/src/%s; git blame --line-porcelain %s | sed -n 's/^author //p'"
# find command formatted with package name and file extension cc, cpp, py, ...
find = 'find ' + DEVEL_DIR + '/src/%s -name "*.%s" -type f'

pkgs = ["hpp-benchmark", "hpp-constraints", "hpp-corbaserver", "hpp-core",
        "hpp-doc", "hpp-hrp2", "hpp-model", "hpp-model-urdf", "hpp_ros",
        "hpp-statistics", "hpp-template-corba", "hpp-tools", "hpp_tutorial",
        "hpp_universal_robot", "hpp-util", "hpp-wholebody-step",
        "hpp-wholebody-step-corba",]

extensions = ["cc", "hh", "cpp", "h", "hpp", "py", "hxx",]

def find_source_files (pkg):
    # Find source files
    source_files = []
    for ext in extensions:
        (status, output) = getstatusoutput (find % (pkg, ext))
        if status == 0:
            output = output.split ('\n')
            output = filter (lambda x:x!='', output)
            source_files.extend (output)
        else:
            raise RuntimeError (output)

    return source_files

def find_authors (pkg, authorMap):
    source_files = find_source_files (pkg)
    for f in source_files:
        (status, output) = getstatusoutput (git_blame % (pkg, f))
        if status == 0:
            for author in output.split('\n'):
                if authorMap.has_key (author):
                    authorMap [author] += 1
                else:
                    authorMap [author] = 1
        else:
            raise RuntimeError (output)

authorMap = dict ()
for pkg in pkgs:
    find_authors (pkg, authorMap)
tmp = authorMap.copy ()
tmp ['Florent Lamiraux'] += tmp ['florent']
tmp.pop ('florent')
tmp.pop ('Not Committed Yet')
try:
    tmp.pop ('fatal: No such ref: HEAD')
except:
    pass

authorList = []
for (k,v) in tmp.items ():
    authorList.append ((k,v))

def compare (x1, y1):
    if x1 [1] < y1[1]: return -1
    if x1 [1] == y1[1]: return 0
    if x1 [1] > y1[1]: return 1

for (k,v) in sorted (authorList, compare):
    print ("%s\t%i"%(k, v))
