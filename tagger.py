#!/usr/bin/python3
#tagger.py

import sys
from mutagen.easyid3 import EasyID3

#def tag()

metatag = EasyID3(sys.argv[1])
metatag['title'] = sys.argv[2]

#print("title : ", metatag['title'])

if len(sys.argv) >= 4:
    metatag['artist'] = sys.argv[3]
#    if len(sys.argv) >= 5:
#        metatag['date'] = int(sys.argv[4])

metatag.save()

#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument list:', str(sys.argv))

#print(arg1)
#print(arg2)
#print(arg3)
