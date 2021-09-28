import datetime
import os
import time

### Como colocar a duração de um processo
start = datetime.datetime.now()
 
print ("Robo iniciado")
i = 0 
while i < 10:
    print("Linha " + str(i))
    i += 1

print("Duração: %s." % (datetime.datetime.now() - start))