import os,glob

dir = '/root/Documents/git/concepts'
os.chdir(dir)
for file in glob.glob('*.py'):
    print(file)