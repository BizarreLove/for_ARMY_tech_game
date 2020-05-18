import zipfile
import os

#def un_zipFiles(path):
path = "./"
files=os.listdir(path)
print(files)
while 1:
    try:
        for file in files:
            if file.endswith('.zip'):
                filePath=path+file
                print(filePath)
                zip_file = zipfile.ZipFile(filePath)
                for names in zip_file.namelist():
                    print(names)
                    path = "./outfolder"
                    zip_file.extract(names,path)
                zip_file.close()
    except:
        break
#name = "./out.zip"

#un_zipFiles(name)


