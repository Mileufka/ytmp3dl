#!/usr/bin/python3
#ytmp3dl.py

import os

with open('download_list.txt') as f:
    datas = f.readlines()

for line in datas:
    metadatas = line.split('%')
    url = 'https://www.youtube.com/watch?v='+metadatas[0]
    name = metadatas[1]
    artist = metadatas[2]
    complement = metadatas[3]
    complement = complement[:-1]

    filename_name = name.replace(' ','_')
    filename_artist = artist.replace(' ','_')
    complement = complement.replace(' ','_')

    filename=filename_name+'_-_'+filename_artist+'_('+complement+')'

    cmd = 'youtube-dl -x --audio-format mp3 --audio-quality 192k --mark-watched --output "~/music/buffer/'+filename+'.mp3" '+url
    
    os.system(cmd)
    #print(cmd)
