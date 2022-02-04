import tkinter
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import cerrar

class ventanaRegistro(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent

    def crearFrame(self):
        frameVentana = tkinter.Frame(self.parent, bg='#e8ebe9', height=400, width=400)
        frameVentana.grid(row=0, sticky='nsew', pady=10, padx=10)

        frameSuperior = tkinter.Frame(frameVentana, bg='#cfcfcf', height=25, width=400)
        frameSuperior.grid(row=0, sticky='ew')

        frameContenido = tkinter.Frame(frameVentana, bg='#e8ebe9', height=375, width=400)
        frameContenido.grid(row=1, sticky='n')
        
        #>---------------Parte Superior------------------<
        frameSuperior.columnconfigure(0, weight=3)
        frameSuperior.columnconfigure(1, weight=1)
        lblTitulo = tkinter.Label(frameSuperior, text='Nuevo Registro', foreground='black', bg='#cfcfcf')
        lblTitulo.grid(column=0, row=0, padx=8, sticky='nw')

        btnCerrar = tkinter.Button(frameSuperior, foreground='white',font=('Arial', 10, 'bold'), text='X', bg='red', width=5, border='0', command=cerrar.cerrarVentana(frameVentana).cerrarFrame)
        btnCerrar.grid(column=1, row=0, sticky='ne')

        #>---------------Contenido de la ventana------------------<
            #>---------Titulos-----------<
        lblNombre = tkinter.Label(frameContenido, text='Nombre', font=('Arial', 10, 'bold'))
        lblNombre.grid(column=0, row=0, padx=10, pady=10, sticky='w')