import os
import glob
  
root_path = 'C:/Users/Pathy/Documents/Musicas'
  
list = ['car', 'truck', 'bike', 'cycle', 'train']

def createDirectorie(pathUrl, namePaste):
    root_path = pathUrl
    path = os.path.join(root_path, namePaste)
    os.mkdir(path)
  
# for items in list:
#     path = os.path.join(root_path, items)
#     os.mkdir(path)

#createDirectorie(root_path, list[0])

list= ['https://padrepauloricardo.org/cursos/historia-da-igreja-antiga', 'https://padrepauloricardo.org/cursos/santo-antonio', 'https://padrepauloricardo.org/cursos/revolucao-e-marxismo-cultural']

def getNameCouse(link):
    return link.split('/')[0:][4]

#getNameCouse('https://padrepauloricardo.org/cursos/historia-da-igreja-antiga')

download_dir = "D:\Download"

def moveFiles(pathDowload):
    arquivo = glob.iglob(os.path.join(download_dir, '*.mp3'))[0]
    shutil.move(arquivo, pathDowload)
    shutil.rmtree(download_dir)

path = 'D:\Padre2'
arquivo = 'teste.mp3'
path_completo = os.path.join(path, arquivo)

moveFiles(path_completo)





