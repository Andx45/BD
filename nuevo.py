import tkinter
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

class NuevoRegistro(tkinter.Frame):
     def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent

     def registrar(self):
         #Propiedades generales de la ventana
         self.NuevoVentana = tkinter.Toplevel(self.parent, bg='#F2F3F4')
         self.NuevoVentana.title('Nuevo Registro')
         self.NuevoVentana.geometry('700x500')

         self.NuevoVentana.grid_rowconfigure(0, weight = 1)
         self.NuevoVentana.grid_columnconfigure(0, weight = 1)

         #Propiedades del espacio de trabajo
         frame1 = tkinter.Frame(self.NuevoVentana, bg='#F2F3F4')
         frame1.grid(row=0, sticky='nw')

         frame2 = tkinter.Frame(self.NuevoVentana, bg='#F2F3F4')
         frame2.grid(column=1, row=0, sticky='nw')

         #------> Creacion de las opciones de registro (Labels) <-------
         lblNoRegistro = tkinter.Label(frame1, text='No. de Registro', font=('Arial', 10, 'bold'))
         lblNoRegistro.grid(column=0, row=0, padx=10, pady=10, sticky='w')

         lblNombre = tkinter.Label(frame1, text='Nombre: ', font=('Arial', 10, 'bold'))
         lblNombre.grid(column=0, row=1, padx=10, pady=10, sticky='w')

         lblSexo = tkinter.Label(frame1, text='Sexo: ', font=('Arial', 10, 'bold'))
         lblSexo.grid(column=0, row=2, padx=10, pady=10, sticky='w')

         lblEspecie = tkinter.Label(frame1, text='Especie: ', font=('Arial', 10, 'bold'))
         lblEspecie.grid(column=0, row=3, padx=10, pady=10, sticky='w')

         lblRaza = tkinter.Label(frame1, text='Raza: ', font=('Arial', 10, 'bold'))
         lblRaza.grid(column=0, row=4, padx=10, pady=10, sticky='w')

         lblDescripcion = tkinter.Label(frame1, text='Descripción: ', font=('Arial', 10, 'bold'))
         lblDescripcion.grid(column=0, row=5, padx=10, pady=10, sticky='w')

         lblFechaNac = tkinter.Label(frame1, text='Fecha de Nacimiento: ', font=('Arial', 10, 'bold'))
         lblFechaNac.grid(column=0, row=6, padx=10, pady=10, sticky='w')

         lblEstado = tkinter.Label(frame1, text='Estado de Ingreso: ', font=('Arial', 10, 'bold'))
         lblEstado.grid(column=0, row=7, padx=10, pady=10, sticky='w')

         lblNotas = tkinter.Label(frame2, text='Notas Adicionales: ', font=('Arial', 10, 'bold'))
         lblNotas.grid(column=0, row=0, padx=10, pady=10, sticky='nw')

         #------> Creacion de las opciones de registro (Entry) <-------
         txtNombre = tkinter.Entry(frame1, width=25, font=('Arial', 10))
         txtNombre.grid(column=1, row=1, padx=5, pady=10, sticky='w')

         sexoVar = tkinter.StringVar()
         boxSexo = ttk.Combobox(frame1, width=25, textvariable=sexoVar)
         boxSexo['values'] = ('Macho', 'Hembra')
         boxSexo.grid(column=1, row=2, padx=5, pady=10, sticky='w')
         boxSexo.current()

         especieVar = tkinter.StringVar()
         boxEspecie = ttk.Combobox(frame1, width=25, textvariable=especieVar)
         boxEspecie['values'] = ('Perro', 'Gato')
         boxEspecie.grid(column=1, row=3, padx=5, pady=10, sticky='w')
         boxEspecie.current()

         txtRaza = tkinter.Entry(frame1, width=25, font=('Arial', 10))
         txtRaza.grid(column=1, row=4, padx=5, pady=10, sticky='w')

         txtNacimiento = DateEntry(frame1, width=22, font=('Arial', 10))
         txtNacimiento.grid(column=1, row=6, padx=5, pady=10, sticky='w')


