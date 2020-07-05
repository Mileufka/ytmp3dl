#!/usr/bin/python3
#ytmp3dl.py

import os
from gui import *
from tagger import apply_tags

root = Tk()
root.geometry("900x700")
main_frame = Main_frame(master=root)
root.mainloop()

#with open('download_list.txt') as f:
#    datas = f.readlines()

#for line in datas:
#    metadatas = line.split('%')
#    url = 'https://www.youtube.com/watch?v='+metadatas[0]
#    name = metadatas[1]
#    artist = metadatas[2]
#    complement = metadatas[3]
#    complement = complement[:-1]
#
#    filename_name = name.replace(' ','_')
#    filename_artist = artist.replace(' ','_')
#    complement = complement.replace(' ','_')
#    filepath = 'storage/'
    #filepath = ''

#    filename=filepath+filename_artist+'_-_'+filename_name+'_('+complement+')'

#    cmd = 'youtube-dl -x --audio-format mp3 --audio-quality 192k --mark-watched --output "'+filename+'.%(ext)s" '+url
    
#    os.system(cmd)

    #filename=filepath+filename_artist+'_-_'+filename_name+'_\('+complement+'\).mp3'
    #os.system('chmod 777 '+filename)

    #filename = filename.replace('\(','(')
    #filename = filename.replace('\)',')')

#    filename+='.mp3'
    #filename=filename.encode('utf8')
#    apply_tags(filename,name,artist)
#print("\n\nEnd of script")
