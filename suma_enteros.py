# ------------------------
# Desktop app No. 1
#------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#-----------------------
# funciones de la app
#-----------------------
 # sumar 
def calcular():
    messagebox.showinfo("Minicalculadora 1.0, " "Las opraciones han sido realizadas")
    s = int( x.get()) + int(y.get())
    r  = int( x.get()) - int(y.get())
    m = int( x.get()) * int(y.get())
    d = int( x.get()) / int(y.get())
    de = int( x.get()) // int(y.get())
    mod = int( x.get()) % int(y.get())
    p = int( x.get()) ** int(y.get())
    t_resultados.insert(INSERT, f"{int(x.get())} + {int(y.get())} = {(s)}")
    
# borrar 
def borrar():
   messagebox.showinfo("Minicalculadora 1.0" , " los datos seran borrados")
   x.set("")
   y.set("")
   t_resultados.delete("1.0" , "end")

# salir 
def salir():
   messagebox.showinfo("Minicalculadora 1.0" , " la app se va a cerrar " )
   ventana_principal.destroy
 
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
lb_x.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_x.place(x=240, y=60)

# caja de texto para valor x
Entry_x = Entry(frame_entrada)
Entry_x.config(bg="white", fg="blue", font=("Times New Roman", 18))
Entry_x.place(x=290,y=60)

# etiqueta para valor de y 
lb_y= Label(frame_entrada, text = "Y" )
lb_y.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_y.place(x=290,y=60)

#---------------------------------
# frame operaciones
#---------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg = "white", width = 480, height = 100)
frame_operaciones.place(x = 10, y = 200)

# boton para sumar
bt_sumar = Button(frame_operaciones, text="Sumar")
bt_sumar.place(x=45, y=35, width=100, height=30)

# boton para borrar
bt_borrar = Button(frame_operaciones, text="Borrar")
bt_borrar.place(x=190, y=35, width=100, height=30)

# boton para salir 
bt_salir = Button(frame_operaciones,text="Salir", command=salir)
bt_salir.place(x=335, y=35, width=100, height=30)

#---------------------------------
# frame resultados 
#---------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg = "white", width = 800, height = 600)
frame_rojo.place(x = 10, y = 310)

# area de texto para los resultados
t_resultados = Text(frame_rojo)
t_resultados.config(bg="black", fg="green", font=("courier, 20"))
t_resultados.place(x=10, y=10, width=400, height=160)

# run
# se ejecuta el metodo mainloop de la clase Tk()a traves de la instancia ventana
ventana_principal.mainloop()