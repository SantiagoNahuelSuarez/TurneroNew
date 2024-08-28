from typing import Tuple
import customtkinter as ctk
import matplotlib.pyplot as plt
from config import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

class Graficos(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.config_windows()
        self.frames()
        self.buttoms()

    def config_windows(self):
        self.title("Graficos")
        self.geometry("900x700")

    def frames(self):
        self.menu_frame = ctk.CTkFrame(
            self,
            width = 250
        )
        self.menu_frame.pack(
            side = "bottom",
            expand = False,
            fill = ctk.BOTH
        )

        self.menu_frame.grid_rowconfigure(3, weight = 1)
        

        self.grafico_frame = ctk.CTkFrame(
            self,
            fg_color = COLOR_BARRA_SUPERIOR
        )
        self.grafico_frame.pack(
            side = "right",
            expand = True,
            fill = ctk.BOTH
        )

    def buttoms(self):

        self.check_grafLine = ctk.CTkButton(
            self.menu_frame,
            text = "Grafico de Linea",
            command = self.graficoLineal

        )
        self.check_grafLine.grid(
            row = 0,
            column = 0,
            pady = 20,
            padx = 30
        )

        self.check_grafBarra = ctk.CTkButton(
            self.menu_frame,
            text = "Grafico de Barra",
            #command = 
        )
        self.check_grafBarra.grid(
            row = 0,
            column = 1,
            padx = 30,
            pady = 10,
        )

        self.check_grafTorta = ctk.CTkButton(
            self.menu_frame,
            text = "Grafico de Torta"
        )
        self.check_grafTorta.grid(
            row = 0,
            column = 2,
            padx = 30,
            pady = 20
        )

        # self.buttom_Genearar = ctk.CTkButton(
        #     self.menu_frame,
        #     text = "Generar Grafico"
        # )
        # self.buttom_Genearar.grid(
        #     row = 0,
        #     column = 3,
        #     sticky = "w",
        #     padx = 30,
        #     pady = 30
        # )
    
    def clear_graph_frame(self):                            #Funcion para limpiar el frame
        for widget in self.grafico_frame.winfo_children():
            widget.destroy()

    def graficoLineal(grafico_frame):

        x = [1, 2, 3, 4, 5, 7]
        y = [20, 50, 70, 89, 91, 100]

        plt.plot(x, y, marker = 'o', color = 'g')
        plt.xlabel("personas")
        plt.ylabel("")

        plt.show()
    
    def show_bar_chart(self, ax):
        categories = ['A', 'B', 'C', 'D']
        values = [3, 7, 5, 9]
        ax.bar(categories, values)
        ax.set_title("Gráfico de Barras")






app = Graficos()
app.mainloop()