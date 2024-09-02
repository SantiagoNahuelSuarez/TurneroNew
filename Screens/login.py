#Ventana de Login

import customtkinter as ctk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#from formularios.Manager import principalscreen
from config import *
from formularios.screens import billing_point
import util.util_imagenes as utl_imagenes
import util.util_ventana as utl_ventana


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green") 


class app(ctk.CTk):
    
    def verificar(self):

        user = self.usuario.get()
        password = self.contraseña.get()

        if(user == 'Root' and password == "1234"):

            self.destroy()
            
            #principalscreen()
        else:
            messagebox.showerror(message = "La contraseña no es correcta", title = "Mensaje")

    
     

    def __init__(self):

        super().__init__()
        self.logo = utl_imagenes.leer_imagen("./imagenes/Logo.png", (600, 350))
        self.config_window()
        self.frames()
        self.labels()
        self.entrys()
        self.buttoms()

    def config_window(self):
        self.title('Login')
        self.iconbitmap("./imagenes/logo.ico")
        self.geometry("500x600+350+20")
        self.minsize(480, 500)
        self.config(bg = '#010101')

    
    def frames(self):

        self.frame_principal = ctk.CTkFrame(
            master = self, 
            fg_color = "#010101",
            corner_radius = 10 
        )
        self.frame_principal.pack(
            expand = True, 
            fill = ctk.BOTH,
            pady = 0
        )

        self.contraseña_frame = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.contraseña_frame.grid(
            columnspan = 2, 
            row = 2,
            padx = 4, 
            pady = 20,
            sticky = "n"
        )

        self.usuario_frame = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.usuario_frame.grid(
            columnspan = 2, 
            row = 1,
            padx = 4, 
            pady = (1, 20),
            sticky = "n"
        )


        self.frame_principal.grid_columnconfigure(0, weight = 1)
        self.frame_principal.grid_rowconfigure(0, weight = 1)

    def labels (self):

        font_awesome = ctk.CTkFont(family = 'FontAwesome', size = 14)
        
        self.label_logo = ctk.CTkLabel(
            self.frame_principal, 
            text = "", 
            image = self.logo, 
        )
        self.label_logo.grid(
            sticky = "n",
            columnspan=2, 
            row = 0,
        )

        self.iconoUser = ctk.CTkLabel(
            self.usuario_frame,
            font = font_awesome,
            text = "\uf007",
            fg_color = "transparent",
            width = 30 
        )
        self.iconoUser.pack(side="left", padx=(0, 5))  # Padding para separar el ícono del texto

        self.iconContraseña = ctk.CTkLabel(
            self.contraseña_frame,
            font = font_awesome,
            text = "\uf023",
            fg_color = "transparent",
            corner_radius = 10,
            width = 30  
        )
        self.iconContraseña.pack(side="left", padx=(0, 5))

    def entrys (self):

        font_awesome = ctk.CTkFont(family = 'FontAwesome', size = 14)

        self.usuario = ctk.CTkEntry(
            self.usuario_frame, 
            font = ctk.CTkFont(family="Arial", size=14),
            placeholder_text = "Usuario",
            fg_color = "#261920",
            corner_radius = 20, 
            height = 40,
            width = 220,  
            justify = "left"
        )
        self.usuario.pack(side="top")
        

        self.contraseña = ctk.CTkEntry(
            self.contraseña_frame, 
            font = ctk.CTkFont(family="Arial", size=14),
            placeholder_text = "Contraseña",
            fg_color = "#261920",
            corner_radius = 20,
            height = 40, 
            width = 220,  # Ajusta el ancho del Entry
            justify="left",
            show="*"
        )
        self.contraseña.pack(side="left")


    def buttoms(self):
        font_awesome = ctk.CTkFont(family = 'FontAwesome', size = 14)

        def mostrar():
            if  self.contraseña.cget("show") == "*":
                self.contraseña.configure(show="")
                self.buttonVer.configure(text="\uf070")
            else:
                self.contraseña.configure(show="*")
                self.buttonVer.configure(text="\uf06e")

        self.buttonVer = ctk.CTkButton(
            self.contraseña,
            font = font_awesome,
            text = "\uf06e",
            width = 5,
            corner_radius = 10,
            fg_color = "transparent",
            command=mostrar
        )
        self.buttonVer.place(
            relx = 1.0,
            rely = 0.04,
            x = -47,
            y = 4
        )
        

        self.buttoninicio = ctk.CTkButton(
            self.frame_principal, 
            text = "Iniciar Sesion", 
            corner_radius = 20, 
            font = font_awesome, 
            height = 35, 
            command = self.verificar
        )
        self.buttoninicio.grid(
            row = 4, 
            column = 0, 
            padx = 20, 
            pady = 50, 
            sticky = "n"              
        )
        self.buttoninicio.bind("<Return>", (lambda event:self.verificar()))

if __name__ == "__main__":
    App = app()        
    App.mainloop()

        


    