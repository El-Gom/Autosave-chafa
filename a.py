#notas antes de empezar
#tienes que instalar python y revistr que tienes pip instalado, puedes revisar que todo esta bien si en el CMD de windows escribes "pip --help" y te aparecen las opciones
#si estas utilizando un IDE para correr el programa, revisa que sepas como detener el proceso, por que es que cuando termine los 99 loops o que directamente sea infinito.

#25/09/22
#La verdad no se que parametros especificamente usa el programa pero generalmente si hay un directorio es para copiar o pegar ese directorio, en mi caso lo use para un server de minecraft con una carpeta de Google Drive en el escritorio



from datetime import datetime
from tkinter import Variable
import pyautogui #pip install pyautogui
import shutil
from distutils.dir_util import copy_tree
import time
import math
from datetime import datetime
import os
import csv

i=0
z=0
g=0
os.chdir(r'Desktop') #directorio de donde quieres que se cree la carpeta de "Miencraft Backup"
dirName = "Backup Minecraft"
dirName2 = "Copy Minecraft"

tiempo = datetime.today().strftime('%Y_%m_%d' + ' ' + '%H_%M_%S')

if not os.path.exists(dirName): #Todo esto es simplemente para saber si ya se creo la carpeta o no
    os.mkdir(dirName)
    print("El directorio " , dirName ,  " fue creado")
else:    
    print("El directorio " , dirName ,  " ya existe")

if not os.path.exists(dirName2): #Todo esto es simplemente para saber si ya se creo la carpeta o no
    os.mkdir(dirName2)
    print("El directorio " , dirName2 ,  " fue creado")
else:    
    print("El directorio " , dirName2 ,  " ya existe")




print("en 5 segundos va a iniciar el programa")
time.sleep(5)


os.chdir(r'Desktop\Forge 1.18.1') #Directorio de donde esta guardado el servidor

print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
print("Trabajando en el siguiente directorio: {0}".format(os.getcwd()))
print('Bienvenido al software de respaldo de minecraft proporcionado por www.paginaver.ga')


while z <= 99: #Cuantas veces quieres que funcione el programa

    while i <= 20: #cuantas veces quieres que se guarde el mundo antes de que se hara respalgo

        pyautogui.typewrite("save-all" + '\n')
        pyautogui.typewrite("say autoguardado completo" + '\n')

        t=600
         #Cual es el tiempo entre cada autosave

        def countdown(t): #Reloj chido xd
            while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                t -= 1
        countdown(int(t))
        time.sleep(1)
        i += 1

    variable = 'respaldo hecho a las '
    filename = variable + format(tiempo)

    print(g)
    os.chdir(r'Desktop/Backup Minecraft/') #esta es la carpeta que se creo cuando inicia el programa
    def get_ignored(path, filenames):
        ret = []
        for filename in filenames:
            if os.path.join(path, filename) in r'Desktop\Backup Minecraft\world': #Carpeta de donde se va a hacer el respaldo del mundo
                ret.append(filename)
            elif filename.endswith(".lock"):
                ret.append(filename)
        return ret


    os.chdir('C:/Users/elchi/Desktop/Copy Minecraft/')
    os.mkdir(format(filename))
    pyautogui.typewrite("say el mundo se va a empezar a respaldar a Google Drive" + '\n')

    shutil.copytree(r'Desktop\Forge 1.18.1\world', format(filename), symlinks=False, ignore=get_ignored, ignore_dangling_symlinks=False,
                    dirs_exist_ok=True)

    shutil.copytree(r'Desktop/Copy Minecraft/', r'Desktop/Backup Minecraft', symlinks=False, ignore=get_ignored, ignore_dangling_symlinks=False,
                    dirs_exist_ok=True)


    shutil.rmtree(filename)


    pyautogui.typewrite("say mundo respaldado" + '\n')#indica que se respaldo el mundo y reinicia
    z+=1 #si quieres que el programa corra infinitamente simplemente elimina este z+=1 y ya
    i=0
    g += 1
quit()