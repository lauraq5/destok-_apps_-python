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
ventana_principal.title ("suma_enteros")

#tamaño de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg = "blue")

#---------------------------------
# frame entradas datos 
#---------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "white", width = 480, height = 180)
frame_entrada.place(x = 10, y = 10)

#logo de la app
logo = PhotoImage(file="ing/escudo_colegio (1).png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=70,y=40)

# titulo de la app 
titulo = Label(frame_entrada, text= "Suma Enteros 1.0")
titulo.config(bg="blue", fg="white", font=("Arial" , 20))
titulo.place(x=240,y=10)

# etiqueta para valor de x
lb_x = Label(frame_entrada, text = "x = " )
lb_x.config(bg="white, fg="blue", font=("Helvetica", 18))
lb_x.Place(x=240, y=60)

# caja de texto para valor x
Entry_x = Entry(frame_entrada)
Entry_x.config(bg="white", fg="blue, font=("Times New Roman", 18))
Entry_x.Place(x=290,y=60)

# etiqueta para valor de y 
lb_y= Label(frame_entrada, text = "Y" =)


#---------------------------------
# frame operaciones
#---------------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg = "white", width = 480, height = 100)
frame_azul.place(x = 10, y = 200)

#---------------------------------
# frame resultados 
#---------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg = "white", width = 800, height = 600)
frame_rojo.place(x = 10, y = 310)

# run
# se ejecuta el metodo mainloop de la clase Tk()a traves de la instancia ventana
ventana_principal.mainloop()