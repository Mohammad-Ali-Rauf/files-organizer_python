import os 
import shutil

path = r'/home/ali'

shutil.disk_usage(path)[0]/(1024 * 1024 * 1024)

listoffiles = os.listdir(path)

for files in listoffiles:
    name, extension=os.path.splitext(files)
    print(name,extension)
    extension=extension[1:]
    
    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+files, path+'/'+extension+'/'+files)
    
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+files, path+'/'+extension+'/'+files)