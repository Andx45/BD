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
        frameContenido.grid(row=1, sticky='nsew')

        imagenUno = tkinter.Canvas(frameContenido, bg='white', height=175, width=175)
        imagenUno.grid(column=0, row=5, padx=10, pady=10)

        imagenDos = tkinter.Canvas(frameContenido, bg='white', height=175, width=175)
        imagenDos.grid(column=1, row=5, padx=10, pady=10)

        #Función para cerrar la ventana
        def cerrar():
            frameVentana.destroy()
        
        #>---------------Parte Superior------------------<
        frameSuperior.columnconfigure(0, weight=3)
        frameSuperior.columnconfigure(1, weight=1)
        lblTitulo = tkinter.Label(frameSuperior, text='Ficha de Registro', foreground='black', bg='#cfcfcf')
        lblTitulo.grid(column=0, row=0, padx=8, sticky='nw')

        btnCerrar = tkinter.Button(frameSuperior, foreground='white',font=('Arial', 10, 'bold'), text='X', bg='red', width=5, border='0', command=cerrar)
        btnCerrar.grid(column=1, row=0, sticky='ne')

        #>---------------Contenido de la ventana------------------<
            #>---------Titulos-----------<
        lblNombre = tkinter.Label(frameContenido, text='Nombre:', font=('Arial', 10, 'bold'))
        lblNombre.grid(column=0, row=0, padx=10, pady=10, sticky='w')

        lblSexo = tkinter.Label(frameContenido, text='Sexo:', font=('Arial', 10, 'bold'))
        lblSexo.grid(column=0, row=1, padx=10, pady=10, sticky='w')

        lblEspecie = tkinter.Label(frameContenido, text='Especie:', font=('Arial', 10, 'bold'))
        lblEspecie.grid(column=0, row=2, padx=10, pady=10, sticky='w')

        lblNacimiento = tkinter.Label(frameContenido, text='Fecha de Nacimiento:', font=('Arial', 10, 'bold'))
        lblNacimiento.grid(column=0, row=3, padx=10, pady=10, sticky='w')

        lblDescripcion = tkinter.Label(frameContenido, text='Notas Adicionales:', font=('Arial', 10, 'bold'))
        lblDescripcion.grid(column=0, row=4, padx=10, pady=10, sticky='nw')

            #>---------Entrys------------<
        txtNombre = tkinter.Entry(frameContenido, width=25, font=('Arial', 10))
        txtNombre.grid(column=1, row=0, padx=5, pady=10)

        sexoVar = tkinter.StringVar()
        comboSexo = ttk.Combobox(frameContenido, width=22, textvariable=sexoVar, font=('Arial', 10))
        comboSexo['values'] = ('Macho', 'Hembra')
        comboSexo.grid(column=1, row=1, padx=5, pady=10)
        comboSexo.current()

        especieVar = tkinter.StringVar()
        comboEspecie = ttk.Combobox(frameContenido, width=22, textvariable=especieVar, font=('Arial', 10))
        comboEspecie['values'] = ('Perro', 'Gato')
        comboEspecie.grid(column=1, row=2, padx=5, pady=10)
        comboEspecie.current()

        txtNacimiento = DateEntry(frameContenido, width=22, font=('Arial', 10))
        txtNacimiento.grid(column=1, row=3, padx=5, pady=10)

        txtNotas = tkinter.Text(frameContenido, width=22, height=8)
        txtNotas.grid(column=1, row=4, padx=5, pady=5)

            #>----------Imagenes-----------<
        

            #>---------Separador----------<
        Separador = ttk.Separator(frameContenido, orient='vertical')
        Separador.grid(column=2, row=0, rowspan=4, sticky='ns')

            #>---------Buttons--------<
        btnExUno = tkinter.Button(frameContenido, width=20, text='Examinar...', bg='#d9db6b', font=('Arial', 10), border='0')
        btnExUno.grid(column=0, row=6, padx=10, pady=5)

        btnExDos = tkinter.Button(frameContenido, width=20, text='Examinar...', bg='#d9db6b', font=('Arial', 10), border='0')
        btnExDos.grid(column=1, row=6, padx=10, pady=5)

        btnNuevo = tkinter.Button(frameContenido, width=8, height=3, text='Registrar')
        btnNuevo.grid(column=3, row=0, rowspan=2, padx=10, pady=10, sticky='nsew')

        btnGuardar = tkinter.Button(frameContenido, width=8, height=3, text='Modificar')
        btnGuardar.grid(column=3, row=2, rowspan=2, padx=10, pady=10, sticky='nsew')


        


        
