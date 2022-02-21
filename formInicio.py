import tkinter
import nuevoRegistro
import buscarRegistro
from PIL import ImageTk, Image

class formularioPrincipal(tkinter.Frame):

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.interfazGrafica()

    def interfazGrafica(self):
        #Propiedades generales de la ventana
        self.parent.title('Registro de animales')
        self.parent.config(bg='white')
        self.parent.geometry('%dx%d' % (self.parent.winfo_screenwidth(), self.parent.winfo_screenheight()))
        self.parent.call('wm', 'iconphoto', self.parent._w, tkinter.PhotoImage(file='img/Paw.png'))

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
        load = Image.open('img/logo.png')
        load = load.resize((50, 50), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        lblImagen = tkinter.Label(frame1, image=render, bg='#ffbf00')
        lblImagen.image = render
        lblImagen.grid(column=0, row=0, pady=4, padx=10)

        titulo = tkinter.Label(frame1, font=('Arial', 12), foreground='white', text='Refugio Sol y Luna', bg='#ffbf00')
        titulo.grid(column=1, row=0, pady=10, padx=10)

        #Creacion de las opciones de la cinta de opciones
        btnAgregarNuevo = tkinter.Button(frame2, width=20, font=('Arial', 9, 'bold'), foreground='white', text='Nuevo Registro', bg='gray', border='0', command = nuevoRegistro.ventanaRegistro(frame3).crearFrame)
        btnAgregarNuevo.grid(column=0, row=0, pady=10, padx=10)

        btnBuscarRegistro = tkinter.Button(frame2, width=20, font=('Arial', 9, 'bold'), foreground='white', text='Buscar Registro', bg='gray', border='0', command = buscarRegistro.ventanaBuscar(frame3).crearFrame)
        btnBuscarRegistro.grid(column=1, row=0, pady=10, padx=10)

        btnConsulta = tkinter.Button(frame2, width=20, font=('Arial', 9, 'bold'), foreground='white', text='Consulta', bg='gray', border='0')
        btnConsulta.grid(column=2, row=0, pady=10, padx=10)

        btnIngresosEgresos = tkinter.Button(frame2, width=20, font=('Arial', 9, 'bold'), foreground='white', text='Ingresos y Egresos', bg='gray', border='0')
        btnIngresosEgresos.grid(column=3, row=0, pady=10, padx=10)

def main():
    root = tkinter.Tk()
    b = formularioPrincipal(root)
    b.mainloop()

if __name__ == '__main__':
    main()