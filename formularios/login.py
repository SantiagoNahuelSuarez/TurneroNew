#Ventana de Login

from tkinter import messagebox
import customtkinter as ctk
from config import *
from formularios.screens import billing_point
import util.util_imagenes as utl_imagenes
import util.util_ventana as utl_ventana
from formularios.Manager import principalscreen

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue") 


class app(ctk.CTk): 

    def verificar(self):

        user = self.usuario.get()
        password = self.contraseña.get()

        if(user == 'Root' and password == "1234"):

            self.destroy()


            principalscreen()
        else:
            messagebox.showerror(message = "La contraseña no es correcta", title = "Mensaje")

    def __init__(self):

        super().__init__()
        self.logo = utl_imagenes.leer_imagen("./imagenes/Logo.png", (500, 350))
        self.config_window()
        self.frames()
        self.labels()
        self.entrys()

    def config_window(self):
        self.title('Login')
        self.iconbitmap("./imagenes/logo.ico")
        self.corner_radius = 10
        w, h = 700, 400
        utl_ventana.centrar_ventana(self, w, h)

    def frames(self):
        self.framelogo = ctk.CTkFrame(
            master = self, 
            width = 400,
        )
        self.framelogo.pack(
            side = "left",
            expand = ctk.NO,
            fill = ctk.BOTH
        )

        self.frame_principal = ctk.CTkFrame(
            master = self, 
            fg_color = "#261920",
            corner_radius = 10 
        )
        self.frame_principal.pack(
            side = "right", 
            expand = True, 
            fill = ctk.BOTH
        )
        self.frame_principal.grid_columnconfigure(0, weight = 1)
        

    def labels (self):
        self.label_logo = ctk.CTkLabel(
            self.framelogo, 
            text = "", 
            image = self.logo, 
        )
        self.label_logo.place(
            x = 0, y = 0, 
            relwidth = 1, 
            relheight = 1
        )

        self.labelTitle = ctk.CTkLabel(
            self.frame_principal, 
            text = "Welcome",
            text_color = "#2D5559",
            font = ctk.CTkFont(family = 'Times New Roman',size = 26, weight = "bold"), 
            
        )
        self.labelTitle.grid(
            row=2, column=0, padx=20, pady=40, sticky="n"
        )

        self.lablelTitle_2 = ctk.CTkLabel(
            self.frame_principal, 
            text = "Iniciar Sesión",
            text_color = "#EEEEEE", 
            font = ctk.CTkFont('Cambria', 20), 
        )
        self.lablelTitle_2.grid(
            row=4, column=0, padx = 20, pady = 20, sticky="w"
        )

    def entrys (self):
        self.usuario = ctk.CTkEntry(
            self.frame_principal, 
            font = ('Baskerville', 14), 
            placeholder_text = "Usuario",
            fg_color = "#261920",
            corner_radius = 10, 
            width = 300
        )
        self.usuario.grid(
            row=6, column=0, padx=20, pady = 20, sticky="ew"
        )

        self.contraseña = ctk.CTkEntry(
            self.frame_principal, 
            font = ('Baskerville', 14), 
            placeholder_text = "Contraseña",
            fg_color = "#261920",
            corner_radius = 10, 
            width = 300
        )
        self.contraseña.grid(
            row=8, column=0, padx=20, pady = 20, sticky="ew"
        )
        self.contraseña.configure(show = "*")

        self.buttoninicio = ctk.CTkButton(self.frame_principal, text = "Iniciar Sesion", corner_radius=10, fg_color = "#2D5559", height = 35, command = self.verificar)
        self.buttoninicio.grid(row=10, column=0, padx=20, pady=30, sticky="s")
        self.buttoninicio.bind("<Return>", (lambda event:self.verificar()))
        
        self.mainloop()


    