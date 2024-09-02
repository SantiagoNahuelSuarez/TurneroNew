import customtkinter as ctk
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class Graficos(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.config_windows()
        self.frames()
        self.labels()
        self.inputus_marker()
        self.checkboxes()
        self.setup_mpl_style()
        self.buttoms()

    def config_windows(self):
        self.title("Graficos")
        self.geometry("900x700")

    def frames(self):

        self.menu_frame = ctk.CTkFrame(
            self,  
            corner_radius = 20,
            fg_color = COLOR_BARRA_SUPERIOR 
        )
        self.menu_frame.pack(side="bottom", expand = False, fill=ctk.BOTH)
        
        self.grafico_frame = ctk.CTkFrame(
             self, 
             fg_color = "#1a1a1a", 
             corner_radius = 10
        )
        self.grafico_frame.pack(side="right", expand = True, fill=ctk.BOTH)

        self.menu_lateral = ctk.CTkFrame(
            self,
            
            corner_radius = 10,
            fg_color = COLOR_GRIS_PASTEL_FRAMES
        )
        self.menu_lateral.pack(side = "left", fill = ctk.BOTH)


    def labels(self):

        Font = ctk.CTkFont( family = 'FontAwesome', size = 14 )

        self.label_datos = ctk.CTkLabel(
        self.menu_lateral,
        fg_color="transparent",
        text="Datos Estadisticos a seleccionar: ",
        text_color=COLOR_GRIS_PASTEL_OSCURO,
        font = Font
        )
        self.label_datos.grid(row=0, column=0, pady=(20, 5), padx=10, sticky="n")

        self.label_select = ctk.CTkLabel(
            self.menu_lateral,
            fg_color="transparent",
            text="Seleccionar grafico: ",
            text_color=COLOR_GRIS_PASTEL_OSCURO,
            font = Font
        )
        self.label_select.grid(row=2, column=0, pady=(50, 5), padx=10, sticky="w")

    def inputus_marker(self):
        self.service_choice = ctk.CTkOptionMenu(
            self.menu_lateral,
            values=['Ganancias por servicios', 'Ganancias por productos', "Ganancias totales"],
            width=200,
            height=20,
            fg_color=COLOR_CUERPO_PRINCIPAL,
            text_color = COLOR_GRIS_PASTEL_OSCURO,
            button_color = COLOR_AZUL_BOTONES,
            dropdown_fg_color = COLOR_CUERPO_PRINCIPAL,
            dropdown_text_color = COLOR_GRIS_PASTEL_OSCURO,
            variable=ctk.StringVar(value='Elija los datos a graficar :')
        )
        self.service_choice.grid(row=1, column=0, pady=(5, 50), padx=10, sticky="n")

    def checkboxes(self):
        
        self.check_grafLine = ctk.CTkCheckBox(
            self.menu_lateral,
            text="Gráfico de Línea",
            text_color=COLOR_GRIS_PASTEL_OSCURO
        )
        self.check_grafLine.grid(row=3, column=0, pady=(10, 5), padx=30, sticky="w")

        self.check_grafBarra = ctk.CTkCheckBox(
            self.menu_lateral,
            text="Gráfico de Barra",
            text_color=COLOR_GRIS_PASTEL_OSCURO
        )
        self.check_grafBarra.grid(row=4, column=0, pady=5, padx=30, sticky="w")

        self.check_grafTorta = ctk.CTkCheckBox(
            self.menu_lateral,
            text="Gráfico de Torta",
            text_color=COLOR_GRIS_PASTEL_OSCURO
        )
        self.check_grafTorta.grid(row=5, column=0, pady=(5, 20), padx=30, sticky="w")

    def buttoms (self):

        self.buttom_Generar = ctk.CTkButton(
            self.menu_frame,
            text="Generar Gráfico",
            fg_color=COLOR_AZUL_BOTONES,
            command=self.generar_grafico,
            corner_radius=15
        )
        self.buttom_Generar.pack(side = "left", pady=20, padx=30)

        self.buttom_imprimir = ctk.CTkButton(
            self.menu_frame,
            text="Imprimir",
            fg_color=COLOR_AZUL_BOTONES,
            corner_radius=15
        )
        self.buttom_imprimir.pack(side = "right", pady=20, padx=30)


    
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
            
        self.grafico_frame.update()
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
