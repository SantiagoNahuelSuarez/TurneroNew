from config import *
import tkinter as tk
import util.util_ventana as util_ventana
 
class billing_point (tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.config_windows()
        self.construirwidget()


    def config_windows(self):
        self.title('Python GUI')
        self.iconbitmap("./imagenes/logo.ico")
        w, h = 400, 100
        util_ventana.centrar_ventana(self, w, h)

    def construirwidget(self):
        self.labelVersion = tk.Label(self, text="Version : 1.0")
        self.labelVersion.config(fg = "#000000",
                                  font= ("Roboto", 15),
                                    pady = 10,
                                      width = 20)
        self.labelVersion.pack()

        self.labelVersion = tk.Label(self, text="Autores : Suarez Rodrigo, Valiente Onir")
        self.labelVersion.config(fg = "#000000",
                                  font= ("Roboto", 15),
                                    pady = 10,
                                      width = 20)
        self.labelVersion.pack()

    