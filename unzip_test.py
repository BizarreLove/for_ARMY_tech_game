import zipfile
import os

#def un_zipFiles(path):
path = "./"


while 1:
    try:
        files=os.listdir(path)
        for file in files:
            if file.endswith('.txt' ,'.PNG' ,'.jpg' ,'.png'):
                #print(file)
                sys.exit()


        for file in files:
            if file.endswith('.zip'):
                filePath=path+file
                print(filePath)
                zip_file = zipfile.ZipFile(filePath)
                for names in zip_file.namelist():
                    #print(names)
                    zip_file.extract(names,path)
                zip_file.close()


    except:
        break
