# -*- coding: utf-8 -*-
import shutil
import os
import urllib





src_dir = 'D:\Download'
 
dest_dir = 'D:\Padre2'


def moverArquivosComExtensao(pastaOrigem, pastaDestino, tipoArquivo):
    audios = []
    for diretorio, subpastas, arquivos in os.walk(pastaOrigem):
        for cont in range(len(arquivos)-1):
            shutil.move(pastaOrigem+"/"+arquivos[cont], pastaDestino+"/"+arquivos[cont])
            print("Arquivos movido com sucesso!!")  
            


#moverArquivosComExtensao(src_dir, dest_dir, 'mp3')

file_url = 'https://chromedriver.storage.googleapis.com/111.0.5563.19/chromedriver_linux64.zip'

file = 'chromedriver.zip'

fullfilename = os.path.join(src_dir, file)
urllib.urlretrieve(file_url, fullfilename)


def download(href, src_dir, newNameFile):
    fullfilename = os.path.join(src_dir, newNameFile)
    urllib.urlretrieve(href, fullfilename)


