import os
from datetime import datetime

print (os.getcwd())
#os.chdir('/root/Documents/git')
print(os.getcwd())


print(os.listdir(os.getcwd()))

#os.mkdir('new')                rmdir
#os.makedirs('new/subnew')      removedirs

#os.rename('old.txt','new.txt')


#os.stat('rev.py')
mod_time  = os.stat('rev.py').st_mtime

print(datetime.fromtimestamp(mod_time))

for dirpath,dirnames,filenames in os.walk('/root/Documents/git'):
    print(dirpath)
    print(dirnames)
    print(filenames)