import pyautogui
import shutil
from distutils.dir_util import copy_tree
import time
import math
from datetime import datetime
import os
import csv
time.sleep(2)
i=0
z=0
g=0
os.chdir(r'Desktop')
dirName = "Backup Minecraft"


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("El directorio " , dirName ,  " fue creado")
else:    
    print("El directorio " , dirName ,  " ya existe")

os.chdir(r'Desktop\Forge 1.18.1')

print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
print("Trabajando en el siguiente directorio: {0}".format(os.getcwd()))
print('Bienvenido al software de respaldo de minecraft proporcionado por www.paginaver.ga')


while z <= 5: #Cuantas veces quieres que funcione el programa

    while i <= 10: #cuantas veces quieres que se guarde el mundo antes de que se hara respalgo

        pyautogui.typewrite("save-all")
        pyautogui.typewrite("say autoguardado completo")

        t=5 #Cual es el tiempo entre cada autosave

        def countdown(t):
            while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                t -= 1
        countdown(int(t))
        time.sleep(1)
        i += 1

    variable = 'respaldo n. ' + str(g) + ' de hoy'

    print(g)
    os.chdir('C:/Users/elchi/Desktop/Backup Minecraft/')
    shutil.copytree(r'Desktop\Forge 1.18.1\world', r'C:Desktop\Backup Minecraft\world', symlinks=False, ignore=None, ignore_dangling_symlinks=False,
                    dirs_exist_ok=False)
    os.chdir('Desktop/Backup Minecraft/')
    os.rename('world', variable)
    pyautogui.typewrite("say mundo copiado")
    z+=1
    i=0
    g += 1
quit()


