import os, shutil, re, sys
from pathlib import Path
from datetime import date
from pprint import pprint
import zipfile


def setup():
    notes = Path(' '.join(sys.argv[1:])).absolute()
    notes_zip = zipfile.ZipFile(notes)
    path = notes.parent / notes.stem
    if not os.path.exists(str(path)):
        os.mkdir(str(path))
    # if not os.path.exists(str(path)+ '-pretty'):
    #     os.mkdir(str(path)+'-pretty')
    notes_zip.extractall(path)
    shutil.copytree(path, str(path)+'_pretty')
    return str(path)+'_pretty'

def rename(path):
    for i in os.listdir(path):
        pattern = r"(\d\d)-(\w\w\w)-(\d\d\d\d)(.*)"
        if(re.search(pattern, i)):
            m = re.search(pattern, i)
            newName = str(path) + '\\' + m.group(2) + '-'+ m.group(1) + '-' + m.group(3) + m.group(4)
            oldName = str(path) + '\\' + i
            shutil.move(oldName, newName) #will be uncommented after debug

if __name__=="__main__":
    rename(setup())
    print("Executed successfully :)")