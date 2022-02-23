import tkinter
from tkinter import CENTER, NW, ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkcalendar import DateEntry
from PIL import ImageTk, Image

class ventanaRegistro(tkinter.Frame):

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent

    def crearFrame(self):
        # ------> Cierra la ventana activa
        def cerrarV():
            frameVentana.destroy()

        # ------> Abre las fotos y las coloca en los frames
        def abrirArchivo(a):
            filetypes = (
                ('archivos de imagen', '*.jpg *.png *.gif *.tif *.tiff'), 
                ('Todos los archivos', '*.*')
            )
            fileImagen = fd.askopenfilename(filetypes=filetypes)

            load = Image.open(fileImagen)
            load = load.resize((175, 175), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            
            if a == 0:
                lblImagen = tkinter.Label(imagenUno, image=render, bg='#ffbf00')
            else:
                lblImagen = tkinter.Label(imagenDos, image=render, bg='#ffbf00')
            
            lblImagen.image = render
            lblImagen.grid(column=0, row=0)
            
        # --------> Permite arrastrar la ventana
        def drag(event):
            frameVentana.place(x=event.x_root, y=event.y_root, anchor='center')
        
        #------------------Fin de las definiciones----------------------

        frameVentana = tkinter.Frame(self.parent, bg='#e8ebe9', height=400, width=400)
        frameVentana.grid(row=0, sticky='nsew', pady=10, padx=10)

        frameSuperior = tkinter.Frame(frameVentana, bg='#cfcfcf', height=25, width=400)
        frameSuperior.grid(columnspan=4, row=0, sticky='ew')
        frameSuperior.bind('<B1-Motion>', drag)

        frameContenido = tkinter.Frame(frameVentana, bg='#e8ebe9', height=375, width=400)
        frameContenido.grid(row=1, sticky='nsew')

        frameBotones = tkinter.Frame(frameVentana, bg='#e8ebe9', height=375, width=100)
        frameBotones.grid(column=3, row=1, rowspan=8, sticky='nsew')
        
        #>---------------Parte Superior------------------<
        frameSuperior.columnconfigure(0, weight=3)
        frameSuperior.columnconfigure(1, weight=1)
        lblTitulo = tkinter.Label(frameSuperior, text='Ficha de Registro', foreground='black', bg='#cfcfcf')
        lblTitulo.grid(column=0, row=0, padx=8, sticky='nw')

        btnCerrar = tkinter.Button(frameSuperior, foreground='white',font=('Arial', 10, 'bold'), text='X', bg='red', width=5, border='0', command=cerrarV)
        btnCerrar.grid(column=1, row=0, sticky='ne')

        #>---------------Contenido de la ventana------------------<
            #>---------Titulos-----------<
        lblNombre = tkinter.Label(frameContenido, text='Nombre:', font=('Arial', 10, 'bold'))
        lblNombre.grid(column=0, row=0, padx=10, pady=6, sticky='w')

        lblSexo = tkinter.Label(frameContenido, text='Sexo:', font=('Arial', 10, 'bold'))
        lblSexo.grid(column=0, row=1, padx=10, pady=6, sticky='w')

        lblEspecie = tkinter.Label(frameContenido, text='Especie:', font=('Arial', 10, 'bold'))
        lblEspecie.grid(column=0, row=2, padx=10, pady=6, sticky='w')

        lblNacimiento = tkinter.Label(frameContenido, text='Fecha de Nacimiento:', font=('Arial', 10, 'bold'))
        lblNacimiento.grid(column=0, row=3, padx=10, pady=6, sticky='w')

        lblAdopcion = tkinter.Label(frameContenido, text='Estado de adopción:', font=('Arial', 10, 'bold'))
        lblAdopcion.grid(column=0, row=4, padx=10, pady=6, sticky='nw')

        lblDescripcion = tkinter.Label(frameContenido, text='Notas Adicionales:', font=('Arial', 10, 'bold'))
        lblDescripcion.grid(column=0, row=5, padx=10, pady=6, sticky='nw')

            #>---------Entrys------------<
        txtNombre = tkinter.Entry(frameContenido, width=25, font=('Arial', 10))
        txtNombre.grid(column=1, row=0, padx=5, pady=6)

        sexoVar = tkinter.StringVar()
        comboSexo = ttk.Combobox(frameContenido, width=22, textvariable=sexoVar, font=('Arial', 10))
        comboSexo['values'] = ('Macho', 'Hembra')
        comboSexo.grid(column=1, row=1, padx=5, pady=6)
        comboSexo.current()

        especieVar = tkinter.StringVar()
        comboEspecie = ttk.Combobox(frameContenido, width=22, textvariable=especieVar, font=('Arial', 10))
        comboEspecie['values'] = ('Perro', 'Gato')
        comboEspecie.grid(column=1, row=2, padx=5, pady=6)
        comboEspecie.current()

        txtNacimiento = DateEntry(frameContenido, width=22, font=('Arial', 10))
        txtNacimiento.grid(column=1, row=3, padx=5, pady=6)

        adopcionVar = tkinter.StringVar()
        comboAdopcion = ttk.Combobox(frameContenido, width=22, textvariable=adopcionVar, font=('Arial', 10))
        comboAdopcion['values'] = ('Adoptado', 'No adoptado')
        comboAdopcion.grid(column=1, row=4, padx=5, pady=6)
        comboAdopcion.current()

        txtNotas = tkinter.Text(frameContenido, width=22, height=8)
        txtNotas.grid(column=1, row=5, padx=5, pady=5)

            #>----------Imagenes-----------<
        imagenUno = tkinter.Canvas(frameContenido, bg='white', height=175, width=175, bd=1, relief='groove')
        imagenUno.grid(column=0, row=6, padx=10, pady=6)

        imagenDos = tkinter.Canvas(frameContenido, bg='white', height=175, width=175, bd=1, relief='groove')
        imagenDos.grid(column=1, row=6, padx=10, pady=6)

            #>---------Separador----------<
        Separador = ttk.Separator(frameContenido, orient='vertical')
        Separador.grid(column=2, row=0, rowspan=7, sticky='ns')

            #>---------Buttons--------<
                #>-------- Imagenes ---------<
        btnExUno = tkinter.Button(frameContenido, width=20, text='Examinar...', bg='#d9db6b', font=('Arial', 10), border='0', command=lambda:abrirArchivo(0))
        btnExUno.grid(column=0, row=7, padx=10, pady=5)

        btnExDos = tkinter.Button(frameContenido, width=20, text='Examinar...', bg='#d9db6b', font=('Arial', 10), border='0', command=lambda:abrirArchivo(1))
        btnExDos.grid(column=1, row=7, padx=10, pady=5)

                #>--------- Operaciones -----------<
        #loadNuevo = Image.open('img/btns/add.png')
        #loadNuevo = loadNuevo.resize((6, 6), Image.ANTIALIAS) 
        #renderNuevo = ImageTk.PhotoImage(loadNuevo)

        photoNuevo = tkinter.PhotoImage(Image.open('img/btns/add.png'))
        btnNuevo = tkinter.Button(frameBotones, width=8, height=3, text='Registrar', image=photoNuevo)
        btnNuevo.grid(column=0, row=0, rowspan=2, padx=25, pady=8, sticky='nsew')

        btnGuardar = tkinter.Button(frameBotones, width=8, height=3, text='Modificar')
        btnGuardar.grid(column=0, row=2, rowspan=2, padx=25, pady=8, sticky='nsew')

        btnEliminar = tkinter.Button(frameBotones, width=8, height=3, text='Eliminar')
        btnEliminar.grid(column=0, row=4, rowspan=2, padx=25, pady=8, sticky='nsew')

        btnHistoria = tkinter.Button(frameBotones, width=8, height=3, text='Historia')
        btnHistoria.grid(column=0, row=6, rowspan=3, padx=25, pady=8, sticky='nsew')



        
