#------------------------
# Desktop app No. 1
#------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *

#-----------------------
# funciones de la app
#-----------------------

#-----------------------------
# ventana principal de la app
#------------------------------

# se declara una variable llamada ventana principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title ("Bandera de noruega ")

#tamaño de la ventana
ventana_principal.geometry("230x600")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la pantalla
ventana_principal.config(bg = "salmon1")

#---------------------------------
# frame azul
#---------------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg = "blue", width = 600, height = 230)
frame_azul.place(x = 0, y = 0)

#---------------------------------
# frame azul
#---------------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg = "blue", width = 600, height = 230)
frame_azul.place(x = 0, y = 0)

#---------------------------------
# frame rojo
#---------------------------------
frame_rojo= Frame(ventana_principal)
frame_rojo.config(bg = "red3", width = 600, height = 230)
frame_rojo.place(x = 0, y = 150)

#---------------------------------
# frame blanco 
#---------------------------------
frame_blanco= Frame(ventana_principal)
frame_blanco.config(bg = "white", width = 600, height = 230)
frame_blanco.place(x = 0, y = 450)

#---------------------------------
# frame blanco 
#---------------------------------
frame_blanco= Frame(ventana_principal)
frame_blanco.config(bg = "white", width = 600, height = 230)
frame_blanco.place(x = 0, y = 450)

#---------------------------------
# frame rojo
#---------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg = "red3", width = 100, height = 250)
frame_rojo.place(x = 100, y = 250)

#run
ventana_principal.mainloop()