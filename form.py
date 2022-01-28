from ctypes import alignment
from tkinter import *
import tkinter.messagebox
from turtle import width
import pandas as pd


#Creación de la ventana
form = Tk()
form.config(bg='white')
form.geometry('%dx%d' % (form.winfo_screenwidth(), form.winfo_screenheight()))
form.title('Registro')
form.iconbitmap('img/refIco.ico')

#Creación de las propiedades del encabezado
frame1 = Frame(form, bg='#ffbf00')
frame1.grid( row=0, sticky='nsew')

#Creación de las propiedades de la cinta de opciones
frame2 = Frame(form, bg='gray')
frame2.grid( row=1, sticky='nsew')

#Creación de las propiedades del espacio para sub-formularios
frame3 = Frame(form, bg='white')
frame3.grid(row=2, sticky='nsew')

#Funciones de botones
def nuevoRegistro():
    frameNuevo = Frame(frame3, bg='#F0F0F0', width=600, height=500)
    frameNuevo.pack(pady=10, padx=10)

#Creación del titulo logo del encabezado
form.columnconfigure(0, weight=1)
imagenL = PhotoImage(file='img/logo.png')
lblImagen = Label(frame1, image=imagenL.subsample(60))
lblImagen.grid(column=0, row=0, pady=10, padx=10)

titulo = Label(frame1, font=('Arial', 12), foreground='white', text='Refugio Sol y Luna', bg='#ffbf00')
titulo.grid(column=1, row=0, pady=10, padx=10)

#Creacion de las opciones de la cinta de opciones
agregarNuevo = Button(frame2, width=20, font=('Arial', 9, 'bold'), foreground='white', text='Nuevo Registro', bg='gray', border='0', command=nuevoRegistro)
agregarNuevo.grid(column=0, row=0, pady=10, padx=10)

buscarRegistro = Button(frame2, width=20, font=('Arial', 9, 'bold'), foreground='white', text='Buscar Registro', bg='gray', border='0')
buscarRegistro.grid(column=1, row=0, pady=10, padx=10)

consulta = Button(frame2, width=20, font=('Arial', 9, 'bold'), foreground='white', text='Consulta', bg='gray', border='0')
consulta.grid(column=2, row=0, pady=10, padx=10)

ingresosEgresos = Button(frame2, width=20, font=('Arial', 9, 'bold'), foreground='white', text='Ingresos y Egresos', bg='gray', border='0')
ingresosEgresos.grid(column=3, row=0, pady=10, padx=10)


form.mainloop()