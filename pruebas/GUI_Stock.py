import customtkinter as ctk
from tkinter import ttk, messagebox
from New_product import New_product_window
from util import util_ventana
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import *


ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

class Stock(ctk.CTkToplevel):

    def __init__(self):
        super().__init__()
        self.config_windows()
        self.frames()
        self.Board()
        self.buttons()
        self.extras()


    def config_windows(self):

        self.title('Gestion Stock Productos')
        self.iconbitmap("./imagenes/logo.ico")
        self.geometry("800x600")
        w, h = 800, 600
        util_ventana.centrar_ventana(self, w, h)
        self.config(bg = COLOR_CUERPO_PRINCIPAL)

    
    def frames(self):

        self.TitleFrame = ctk.CTkFrame(self, fg_color = COLOR_GRIS_PASTEL_MEDIO, bg_color = COLOR_CUERPO_PRINCIPAL, corner_radius = 20)
        self.TitleFrame.pack(side = "top", fill = ctk.X, pady = (30, 30), padx = 20)
        

        self.buttomsFrame = ctk.CTkFrame(self, fg_color = COLOR_BARRA_SUPERIOR, corner_radius = 20)
        self.buttomsFrame.pack(side = "bottom", fill = ctk.BOTH)

        self.BoarFrame = ctk.CTkFrame(self, fg_color = COLOR_GRIS_PASTEL_MEDIO, bg_color = COLOR_CUERPO_PRINCIPAL, corner_radius = 20)
        self.BoarFrame.pack(side = "top", fill = ctk.BOTH, pady = 10, padx = 20)


    def Board(self):

        style = ttk.Style()
        style.configure("Custom.Treeview", 
                        background = COLOR_CUERPO_PRINCIPAL,  
                        foreground = COLOR_GRIS_PASTEL_OSCURO,   
                        fieldbackground=COLOR_GRIS_PASTEL_MEDIO,  
                        borderwidth=2,        
                        bordercolor= COLOR_GRIS_PASTEL_OSCURO,
                        relief="solid",
                        rowheight = 35,  
                        font=('Helvetica', 10))  

        style.map("Custom.Treeview", 
                background=[("selected", COLOR_GRIS_PASTEL_OSCURO)],
                foreground=[("selected", "white")])
        
        style.layout("Custom.Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        
        self.board = ttk.Treeview(self.BoarFrame, columns=("Codigo", "Nombre", "Cantidad", "Precio"), show='headings', style="Custom.Treeview")
        self.board.heading("Codigo", text="Codigo", anchor="center")
        self.board.heading("Nombre", text="Nombre", anchor="center")
        self.board.heading("Cantidad", text="Cantidad", anchor="center")
        self.board.heading("Precio", text="Precio", anchor="center")

        self.board.column("Codigo", anchor="center", width=100)  # Ajuste de los anchos
        self.board.column("Nombre", anchor="w", width=200)
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

        for product in products:
            self.board.insert("", "end", values=product)

        self.board.pack(expand=True, fill=ctk.BOTH, padx=30, pady=30)



    def buttons(self):

        self.add_btn = ctk.CTkButton(self.buttomsFrame, text="Agregar Producto", fg_color = COLOR_AZUL_BOTONES, corner_radius = 10, command = New_product_window)
        self.add_btn.grid(row=0, column=0, padx=60, pady=20, sticky = "e")

        self.edit_btn = ctk.CTkButton(self.buttomsFrame, text="Editar Producto", fg_color = COLOR_AZUL_BOTONES, corner_radius = 10)
        self.edit_btn.grid(row=0, column=1, padx=60, pady=20, sticky = "n")

        self.delete_btn = ctk.CTkButton(self.buttomsFrame, text="Eliminar Producto", fg_color = COLOR_AZUL_BOTONES, corner_radius = 10, command = self.delete_product)
        self.delete_btn.grid(row=0, column=2, padx=60, pady=20, sticky = "w")

    def search_product(self, event=None):
        
        search_term = self.search_entry.get().lower()  # Obtener el texto de búsqueda
        for item in self.board.get_children():
            product_name = self.board.item(item, "values")[1].lower()  # Nombre del producto en minúsculas
            if search_term in product_name:  # Si el término de búsqueda coincide con parte del nombre
                self.board.selection_set(item)  # Seleccionar el producto en el Treeview
                self.board.see(item)  # Asegurarse de que el ítem seleccionado sea visible
                break  # Detener la búsqueda al encontrar el primer resultado
        else:
            messagebox.showwarning("Advertencia", "Producto no encontrado.")

    def delete_product(self):
        # Obtener el ítem seleccionado
        selected_item = self.board.selection()
        
        if not selected_item:
            messagebox.showwarning("Advertencia", "Debe seleccionar un producto para darlo de baja.")
        else:
            # Confirmar si desea eliminar el ítem
            confirm = messagebox.askyesno("Confirmación", "¿Está seguro de que desea dar de baja este producto?")
            if confirm:
                self.board.delete(selected_item)  # Eliminar el ítem del Treeview
                messagebox.showinfo("Éxito", "Producto dado de baja correctamente.")    

    
    def extras(self):

        self.label = ctk.CTkLabel(self.TitleFrame, text="Gestión de Stock", font=ctk.CTkFont(size=24, weight="bold"), text_color = COLOR_GRIS_PASTEL_OSCURO)
        self.label.grid(row=0, column=0, padx = 30, pady = 30)

        self.search_entry = ctk.CTkEntry(self.TitleFrame, placeholder_text="Buscar producto...", width = 200)
        self.search_entry.bind("<Return>", self.search_product)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10)


    

App = Stock()        
App.mainloop()