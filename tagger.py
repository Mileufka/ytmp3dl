#!/usr/bin/python3
#tagger.py

import mutagen
from mutagen.easyid3 import EasyID3

def apply_tags(filename,title,artist):

    print('\n\n'+filename+'\n\n')
    
    try:
        metatag = EasyID3(filename)
    except:
        metatag = mutagen.File(filename, easy=True)
        metatag = add_tags()

    metatag['title'] = title
    metatag['artist'] = artist
    metatag.save()

#print("title : ", metatag['title'])

#    if len(sys.argv) >= 4:
#        metatag['artist'] = artist
#    if len(sys.argv) >= 5:
#        metatag['date'] = int(sys.argv[4])

#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument list:', str(sys.argv))

#print(arg1)
#print(arg2)
#print(arg3)
