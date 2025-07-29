# from os import walk
from os import listdir
import random

def getFilesInDir(mypath):
    f = []
    f = ['/'.join([mypath,file]) for file in listdir(mypath)]
    return f

def selectRandomMask(img_files):
    return random.choice(img_files)

