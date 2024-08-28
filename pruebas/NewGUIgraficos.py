import customtkinter as ctk
import matplotlib.pyplot as plt
from config import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class Graficos(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.config_windows()
        self.frames()
        self.checkboxes()
        self.setup_mpl_style()

    def config_windows(self):
        self.title("Graficos")
        self.geometry("900x700")

    def frames(self):

        self.menu_frame = ctk.CTkFrame(
            self, 
            width = 250, 
            corner_radius = 20,
            fg_color = COLOR_BARRA_SUPERIOR 
        )
        self.menu_frame.pack(side="bottom", expand = False, fill=ctk.BOTH)
        
        self.grafico_frame = ctk.CTkFrame(
            self, 
            fg_color = COLOR_CUERPO_PRINCIPAL, 
            corner_radius = 20
        )
        self.grafico_frame.pack(side="right", expand = True, fill=ctk.BOTH)

        self.menu_lateral = ctk.CTkFrame(
            self,
            height = 250,
            corner_radius = 20,
            fg_color = COLOR_GRIS_PASTEL_FRAMES
        )
        self.menu_lateral.pack(side = "left", expand = False, fill = ctk.BOTH )
        
    def checkboxes(self):
        
        self.check_grafLine = ctk.CTkCheckBox(
            self.menu_frame, 
            text="Grafico de Línea"
        )
        self.check_grafLine.grid(row = 0, column = 0, pady = 10, padx = 30, sticky="e")

        self.check_grafBarra = ctk.CTkCheckBox(
            self.menu_frame, 
            text = "Grafico de Barra"
        )
        self.check_grafBarra.grid(row = 0, column = 1, pady = 10, padx = 30, sticky="e")

        self.check_grafTorta = ctk.CTkCheckBox(
            self.menu_frame, 
            text = "Grafico de Torta"
        )
        self.check_grafTorta.grid(row = 0, column = 2, pady = 10, padx = 30, sticky = "e")

        self.buttom_Genearar = ctk.CTkButton(
            self.menu_frame, 
            text = "Generar Grafico", 
            command = self.generar_grafico,
            corner_radius = 15
        )
        self.buttom_Genearar.grid(row = 0, column = 3, pady = 20, padx = 30, sticky="w")
    
    def setup_mpl_style(self):
        # Aplicar un estilo moderno
        plt.style.use('ggplot')
        plt.rcParams.update({
            "axes.edgecolor": "#ffffff",  # Color de los bordes de los ejes
            "axes.linewidth": 1.5,        # Grosor de los ejes
            "axes.labelcolor": "#ffffff", # Color de las etiquetas de los ejes
            "xtick.color": "#ffffff",     # Color de los valores en el eje x
            "ytick.color": "#ffffff",     # Color de los valores en el eje y
            "figure.facecolor": "#1a1a1a" # Color de fondo de la figura
        })

    def generar_grafico(self):
        # Limpiar el frame antes de dibujar un nuevo gráfico
        for widget in self.grafico_frame.winfo_children():
            widget.destroy()
        
        # Generar un gráfico de ejemplo basado en los checkboxes
        fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
        
        if self.check_grafLine.get():
            ax.plot([1, 2, 3], [1, 4, 9], label='Línea', color='#ff6f61', linewidth=2.5)

        if self.check_grafBarra.get():
            ax.bar([1, 2, 3], [1, 4, 9], label='Barra', color='#6f83ff', alpha=0.7)

        if self.check_grafTorta.get():
            ax.pie([15, 30, 45, 10], labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%', startangle=90)

        ax.set_title('Gráfico Moderno', fontsize=18, color='#ffffff')
        ax.legend(facecolor="#1a1a1a", framealpha=0, fontsize=12)

        # Mostrar el gráfico en la GUI
        canvas = FigureCanvasTkAgg(fig, master=self.grafico_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill=ctk.BOTH)

app = Graficos()
app.mainloop()
