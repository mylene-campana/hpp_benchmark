#!/usr/bin/env python

from os import walk
from os.path import join, isfile
directories = []
for (dirpath, dirnames, filenames) in walk('.'):
    directories.extend (dirnames)

directories = filter (lambda x:isfile (join (x, 'comment')), directories)

directories.sort ()
for d in directories:
    print ("--- %s ---"%d)
    with open (join (d, 'comment')) as f:
        print (f.read ())
    subdirs = []
    for (dirpath, dirnames, filenames) in walk(d):
        subdirs.extend (dirnames)
    subdirs.sort ()
    for d1 in subdirs:
        print ("  --- %s ---"%d1)
        with open (join (d, d1, 'benchmark')) as benchmark:
            for line in benchmark:
                if line [:7] == "Average":
                    print ("  " + line[:-1])
            print ('\n')
    
        
#os.path.isdir ()
#os.path.isfile ()
