import zipfile
import os

path = "./"
files=os.listdir(path)

def un_zipFiles(path):
    for file in files:
        if file.endswith('.zip'):
            filePath = path+file
            print(filePath)
            zip_file = zipfile.ZipFile(filePath)
            for names in zip_file.namelist():
                print(names)
                path = "./outfolder"
                zip_file.extract(names,path)
            zip_file.close()

path = "./"
while 1:
    
    un_zipFiles(path)
    path = path + "outfolder/"
    
    


