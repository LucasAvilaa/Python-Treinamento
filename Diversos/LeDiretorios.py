import fnmatch
import os

print("______Lendo diretorio______" + '\n')

for file in os.listdir('.'): # o '.' nesse caso é o diretorio q esta salvo esse arquivo
    if fnmatch.fnmatch(file, '*.txt'): ##O que eu colocar entre '' vai ser oq o robo vai procurar
        # fnmatch.fnmatch(file, '[!.]*.xlsx') Procura todos os arquivos excel
        #
        print(file,"%-25s","teste")
        open(file, "a").writelines("python")
