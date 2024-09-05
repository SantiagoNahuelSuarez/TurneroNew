import customtkinter as ctk
from tkinter import ttk
#import util.util_ventana as utl
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import *


ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

class Stock(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.config_windows()
        self.frames()
        self.Board()
        self.buttoms()
        self.extras()


    def config_windows(self):

        self.title('Gestion Stock Productos')
        self.iconbitmap("./imagenes/logo.ico")
        self.geometry("800x600")
        #w, h = 800, 600
        #utl.centrar_ventana(self, w, h)
        self.config(bg = COLOR_CUERPO_PRINCIPAL)

    
    def frames(self):

        self.TitleFrame = ctk.CTkFrame(self, fg_color = COLOR_GRIS_PASTEL_FRAMES, bg_color = COLOR_CUERPO_PRINCIPAL, corner_radius = 20)
        self.TitleFrame.pack(side = "top", fill = ctk.X, pady = (10, 30), padx = 20)
        #self.TitleFrame.pack_configure(False)

        self.buttomsFrame = ctk.CTkFrame(self, fg_color = COLOR_BARRA_SUPERIOR, corner_radius = 20)
        self.buttomsFrame.pack(side = "bottom", fill = ctk.BOTH)

        self.BoarFrame = ctk.CTkFrame(self, fg_color = COLOR_GRIS_PASTEL_FRAMES, bg_color = COLOR_CUERPO_PRINCIPAL, corner_radius = 20)
        self.BoarFrame.pack(side = "top", fill = ctk.BOTH, pady = 50, padx = 20)


    def Board(self):

        style = ttk.Style()
        style.configure("Custom.Treeview", 
                        background="white",  # Fondo
                        foreground="gray",   # Texto
                        fieldbackground="gray25",  # Fondo de las celdas
                        borderwidth=2,        # Ancho del borde
                        bordercolor = "gray25",
                        relief="solid")       # Tipo de borde

        style.map("Custom.Treeview", 
                  background=[("selected", COLOR_GRIS_PASTEL_OSCURO)],
                  foreground=[("selected", "white")])
        
        style.layout("Custom.Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        
        
        self.board = ttk.Treeview(self.BoarFrame, columns=("Codigo", "Nombre", "Cantidad", "Precio"), show='headings', style = "Custom.Treeview")
        self.board.heading("Codigo", text="Codigo")
        self.board.heading("Nombre", text="Nombre")
        self.board.heading("Cantidad", text="Cantidad")
        self.board.heading("Precio", text="Precio")

        self.board.column("Codigo", anchor="center", width=50)
        self.board.column("Nombre", anchor="w", width=150)
        self.board.column("Cantidad", anchor="center", width=100)
        self.board.column("Precio", anchor="center", width=100)

        products = [
            ("001", "Shampoo", 50, "$10.00"),
            ("002", "Gel Fijador", 30, "$5.50"),
            ("003", "Aceite para Barba", 20, "$12.00"),
            ("004", "Cera para Cabello", 25, "$8.00"),
            ("005", "Peine", 100, "$2.00"),
            ("006", "Polvo texturisador", 300, "$8.00"),
            ("007", "Tijeras", 400, "$4.00"),
            ("008", "Maquina", 10, "$20.00"),
            ("009", "Toalla", 80, "$2.00")
        ]

        # Insertar cada producto en el Treeview
        for product in products:
            self.board.insert("", "end", values = product)

        self.board.pack(expand=True, fill= ctk.BOTH, padx = 60, pady = 60)

        

        #self.scrollbar_vertical = ttk.Scrollbar(self.board, orient="vertical") #Scroll del Treeview
        #self.scrollbar_vertical.pack(side="right", fill="y")

        #self.scrollbar_vertical.config(command=self.board.yview)


    def buttoms(self):

        self.add_btn = ctk.CTkButton(self.buttomsFrame, text="Agregar Producto", fg_color = COLOR_AZUL_BOTONES, corner_radius = 10)
        self.add_btn.grid(row=0, column=0, padx=60, pady=20, sticky = "e")

        self.edit_btn = ctk.CTkButton(self.buttomsFrame, text="Editar Producto", fg_color = COLOR_AZUL_BOTONES, corner_radius = 10)
        self.edit_btn.grid(row=0, column=1, padx=60, pady=20, sticky = "n")

        self.delete_btn = ctk.CTkButton(self.buttomsFrame, text="Eliminar Producto", fg_color = COLOR_AZUL_BOTONES, corner_radius = 10)
        self.delete_btn.grid(row=0, column=2, padx=60, pady=20, sticky = "w")

    
    def extras(self):

        self.label = ctk.CTkLabel(self.TitleFrame, text="Gestión de Stock", font=ctk.CTkFont(size=24, weight="bold"), text_color = COLOR_GRIS_PASTEL_OSCURO)
        self.label.grid(row=0, column=0, padx = 30, pady = 30)

        self.search_entry = ctk.CTkEntry(self.TitleFrame, placeholder_text="Buscar producto...")
        self.search_entry.grid(row=0, column=1, padx=10, pady=10)

    

App = Stock()        
App.mainloop()