import os, shutil, re, sys
from pathlib import Path
from datetime import date
from pprint import pprint


pattern = r"(\d\d)-(\w\w\w)-(\d\d\d\d)(.*)"
path = Path(' '.join(sys.argv[1:])).absolute()
if not os.path.exists(str(path)+'-pretty'):
    os.mkdir(str(path)+'-pretty')

for i in os.listdir(path):
    if(re.search(pattern, i)):
        m = re.search(pattern, i)
        newName = str(path) + '-pretty\\' + m.group(2) + '-'+ m.group(1) + '-' + m.group(3) + m.group(4)
        oldName = str(path) + '\\' + i
        print(newName)
        #shutil.move(oldName, newName) will be uncommented after debug