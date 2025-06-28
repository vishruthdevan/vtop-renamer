import os, shutil, re, sys
from pathlib import Path
from datetime import date
from pprint import pprint
import zipfile

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
def setup():
    notes = Path(' '.join(sys.argv[1:])).absolute()
    notes_zip = zipfile.ZipFile(notes)
    path = notes.parent / notes.stem
    if not os.path.exists(str(path)):
        os.mkdir(str(path))
    # if not os.path.exists(str(path)+ '-pretty'):
    #     os.mkdir(str(path)+'-pretty')
    notes_zip.extractall(path)
    shutil.copytree(path, str(path)+'_pretty', dirs_exist_ok=True)

    return str(path)+'_pretty'

def rename(path):
    namelist = list()
    datelist = list()
    pattern = r"(\d\d)-(\w\w\w)-(\d\d\d\d)(.*)"
    for i in os.listdir(path):
        if(m := re.search(pattern, i)):
            d = date(int(m.group(3)), int(months.index(m.group(2)))+1, int(m.group(1)))
            oldName = str(path) + "\\" + i
            namelist.append(oldName)
            datelist.append(d)
    sorted_names = sorted(list(zip(namelist, datelist)), key = lambda x: x[1])
    count = 1
    for i, j in sorted_names:
        m = re.search(pattern, i)
        newName = str(path) + '\\' + str(count) + '. ' + m.group(2) + '-'+ m.group(1) + '-' + m.group(3) + m.group(4)
        shutil.move(i, newName)
        count+=1
    

if __name__=="__main__":
    rename(setup())
    print("Executed successfully :)")