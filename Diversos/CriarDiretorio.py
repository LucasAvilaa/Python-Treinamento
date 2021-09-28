import time
import datetime
import sys, win32com.client
import time
import json
import requests
import os
import csv


##Cria e apaga diretórios

print("O diretório corrente é: " + os.getcwd())
#print("O diretório corrente é: " + os.getcwd())


## os.chdir()    Muda o diretório
## os.getcwd()   current working directory - diretorio atualmente em processo - diretorio atual
dire = os.getcwd()
dire2 = dire + "\\Teste\\{date:%d-%m-%Y_%H-%M-%S}".format(date = datetime.datetime.now())

try:
    if not os.path.exists(dire2):
        print("Deseja adicionar um novo diretório? \n")
        res = input()
        if res == "sim":
            os.makedirs(dire2)
            print("Criando diretório")
            time.sleep(3)
            print("O novo diretório é " + dire2)
        else:
            print("OK")

    else:
        print("Deseja apagar o diretório?")
        a = input()
        if a == "sim":
            os.removedirs(dire2)
            print("Diretório removido")
        else:
            print("OK")
except:
    pass

