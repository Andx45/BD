import tkinter

class cerrarVentana(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
    
    def cerrarFrame(self):
        for widgets in self.parent:
            widgets.destroy()