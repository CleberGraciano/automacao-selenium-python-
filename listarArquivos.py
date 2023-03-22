import os

pasta = 'C:\Users\Pathy\Downloads'



for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
       if arquivo.lower().endswith('.mp3'):
        print(arquivo)
   