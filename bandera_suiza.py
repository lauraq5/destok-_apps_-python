# ------------------------
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
ventana_principal.title ("Bandera de suiza")

#tamaño de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la pantalla
ventana_principal.config(bg = "red")

#---------------------------------
# frame blanco1
#---------------------------------
frame_blanco1= Frame(ventana_principal)
frame_blanco1.config(bg = "white", width = 100, height = 300)
frame_blanco1.place(x = 200, y =100)

#---------------------------------
# frame blanco2
#---------------------------------
frame_blanco2= Frame(ventana_principal)
frame_blanco2.config(bg = "white", width = 300, height = 300)
frame_blanco2.place(x = 200, y = 100)

# run
ventana_principal.mainloop()