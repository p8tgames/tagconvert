#from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
#import mutagen.id3
from mutagen.id3 import ID3, ID3NoHeaderError
import os
#import pprint
def start():
    #pprint.pprint(ID3.valid_keys.keys()) Debug purposes
    musiclist = input("Enter the dir of your media files: ")

    try:
        musiclistdir = os.listdir(musiclist)
        print("Going to process these files: ")
        for abc in musiclistdir:
            print(abc)
    except NotADirectoryError:
        print("The program could not find the dir you specified. Is it entered correctly?????????")
        print(Exception)
        start()
    listoftracks = len(musiclistdir)
    print("{} Files are going to pre processed. MAKE SURE THERE ARE NO FILES OTHER THAN MEDIA FILES IN THE DIR. FILES SHOULD BE SPLIITED LIKE THIS: TrackNumber - AlbumName - TitleName (exanple: 100 - Undertale OST - MEGALOVANIA)".format(listoftracks))
    inp2 = input("Enter 'YES' to proceed.")
    if inp2 == "YES":
        oeufstart(musiclistdir, listoftracks, musiclist)
    elif inp2 == "yes":
        print("DO NOT TYPE IT IN LOWERCASE IDIOT")
    elif inp2 == "y":
        print("DONT TYPE y ONLY YOU LAZY IDIOT")
    else:
        print("LMAO NERD DIDNT TYPE YES")

def oeufstart(filedir, dilenr, direc):
    print("Passed succ")
    print(filedir)
    print(dilenr)
    artistname = input("Enter artist name: ")
    for ded in filedir:
        ded2 = ded.split(" - ")
        ded3 = ded.split(".")
        if direc.endswith("/"):
            pass
        else:
            direc = direc + "/"
        filenamenow = direc + ded
        print(ded2)
        print("File extension for current file: {}".format(ded3[1]))
        print("---------------------------------------")
        try:
            tags = EasyID3(filenamenow)
            tags['title'] = ded2[2]
            tags['artist'] = artistname
            tags['album'] = ded2[1]
            tags['tracknumber'] = ded2[0]
        except ID3NoHeaderError:
            tags = EasyID3()
        tags.save(filenamenow)
        os.rename(filenamenow, direc + ded2[2])
start()
