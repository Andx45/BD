import tkinter

class NuevoRegistro(tkinter.Frame):
     def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent

     def registrar(self):
         self.NuevoVentana = tkinter.Toplevel(self.parent)
         self.NuevoVentana.title('Nuevo Registro')
         self.NuevoVentana.geometry('500x500')
         self.NuevoVentana.grid_rowconfigure(0, weight = 1)
         self.NuevoVentana.grid_columnconfigure(0, weight = 1)
