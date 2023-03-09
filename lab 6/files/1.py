import os
#list directories
files = os.listdir()
print(files)

#List all files
for file in files:
    if os.path.isfile(file):
        print(file)
        
 #list all
path = '/Users/amina/Desktop/lab 6'
dirPathes =[]
dirNames = []
fileNames = []
for (dir_path, dir_name, file_name) in os.walk(path):
    dirPathes.append(dir_path)
    dirNames.append(dir_name)
    fileNames.extend(file_name)
print(dirPathes)
print(dirNames)
print(fileNames)
 