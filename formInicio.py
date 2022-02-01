import tkinter
import nuevo

class formularioPrincipal(tkinter.Frame):

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.interfazGrafica()

    def interfazGrafica(self):
        #Propiedades generales de la ventana
        self.parent.title('Refugio Sol y Luna')
        self.parent.config(bg='white')
        self.parent.geometry('%dx%d' % (self.parent.winfo_screenwidth(), self.parent.winfo_screenheight()))

        #Propiedades del encabezado
        frame1 = tkinter.Frame(self.parent, bg='#ffbf00')
        frame1.grid( row=0, sticky='nsew')

        #Propiedades de la cinta de opciones
        frame2 = tkinter.Frame(self.parent, bg='gray')
        frame2.grid( row=1, sticky='nsew')

        #Propiedades del espacio para sub-formularios
        frame3 = tkinter.Frame(self.parent, bg='white')
        frame3.grid(row=2, sticky='nsew')

        #Creación del titulo logo del encabezado
        self.parent.columnconfigure(0, weight=1)
        imagenL = tkinter.PhotoImage(file='img/logo.png')
        lblImagen = tkinter.Label(frame1, image=imagenL.subsample(60))
        lblImagen.grid(column=0, row=0, pady=10, padx=10)

        titulo = tkinter.Label(frame1, font=('Arial', 12), foreground='white', text='Refugio Sol y Luna', bg='#ffbf00')
        titulo.grid(column=1, row=0, pady=10, padx=10)

        #Creacion de las opciones de la cinta de opciones
        agregarNuevo = tkinter.Button(frame2, width=20, font=('Arial', 9, 'bold'), foreground='white', text='Nuevo Registro', bg='gray', border='0', command = nuevo.NuevoRegistro(frame3).registrar)
        agregarNuevo.grid(column=0, row=0, pady=10, padx=10)

        buscarRegistro = tkinter.Button(frame2, width=20, font=('Arial', 9, 'bold'), foreground='white', text='Buscar Registro', bg='gray', border='0')
        buscarRegistro.grid(column=1, row=0, pady=10, padx=10)

        consulta = tkinter.Button(frame2, width=20, font=('Arial', 9, 'bold'), foreground='white', text='Consulta', bg='gray', border='0')
        consulta.grid(column=2, row=0, pady=10, padx=10)

        ingresosEgresos = tkinter.Button(frame2, width=20, font=('Arial', 9, 'bold'), foreground='white', text='Ingresos y Egresos', bg='gray', border='0')
        ingresosEgresos.grid(column=3, row=0, pady=10, padx=10)

        #Creación del contendor para sub-formularios
        contenedorVentanas = tkinter.LabelFrame(frame3, text='Espacio de Trabajo')
        contenedorVentanas.grid(column=0, row=0, padx=10, pady=10)

        alignment_var = tkinter.StringVar()
        alignments = ('Left', 'Center', 'Right')

        grid_column = 0
        for alignment in alignments:
            # create a radio button
            radio = tkinter.Radiobutton(contenedorVentanas, text=alignment, value=alignment, variable=alignment_var)
            radio.grid(column=grid_column, row=0, ipadx=10, ipady=10)
            # grid column
            grid_column += 1

def main():
    root = tkinter.Tk()
    b = formularioPrincipal(root)
    b.mainloop()

if __name__ == '__main__':
    main()