#Ventana de Login

from tkinter import messagebox
import customtkinter as ctk
<<<<<<< HEAD
from config import *
from formularios.screens import billing_point
=======
import os
from PIL import ImageTk, Image
>>>>>>> 95034aaddd30230c0e47fa1add3cf28fdb37b8c8
import util.util_imagenes as utl_imagenes
import util.util_ventana as utl_ventana
from formularios.Manager import principalscreen

<<<<<<< HEAD
=======
carpeta_principal = os.path.dirname(__file__)
>>>>>>> 95034aaddd30230c0e47fa1add3cf28fdb37b8c8

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue") 

<<<<<<< HEAD
class app(ctk.CTk): 
=======
class app: 
>>>>>>> 95034aaddd30230c0e47fa1add3cf28fdb37b8c8

    def verificar(self):

        user = self.usuario.get()
        password = self.contraseña.get()

        if(user == 'Root' and password == "1234"):
<<<<<<< HEAD
            self.destroy()
=======
            self.root.destroy()
>>>>>>> 95034aaddd30230c0e47fa1add3cf28fdb37b8c8
            principalscreen()
        else:
            messagebox.showerror(message = "La contraseña no es correcta", title = "Mensaje")

    def __init__(self):
<<<<<<< HEAD
        super().__init__()
        self.logo = utl_imagenes.leer_imagen("./imagenes/logo_login.png", (250, 250))
        self.config_window()
        self.frames()
        self.labels()
        self.entrys()

    def config_window(self):
        self.title('Inicio Sesion')
        self.iconbitmap("./imagenes/logo.ico")
        w, h = 800, 500
        utl_ventana.centrar_ventana(self, w, h)

    def frames(self):
        self.framelogo = ctk.CTkFrame(
            master = self, 
            bg_color = '#EEEEEE',
            width = 450
        )
        self.framelogo.pack(
            side = "left",
            expand = ctk.NO,
            fill = ctk.BOTH
        )

        self.frame_principal = ctk.CTkFrame(
            master = self, 
            border_width = 0, 
            bg_color = COLOR_MENU_LATERAL, 
            border_color = COLOR_MENU_LATERAL
        )
        self.frame_principal.pack(
            side = "right", 
            expand = ctk.YES, 
            fill = ctk.BOTH
        )

    def labels (self):
        self.label_logo = ctk.CTkLabel(
            self.framelogo, 
            text = "", 
            image = self.logo, 
            bg_color = '#EEEEEE'
        )
        self.label_logo.place(
            x = 0, y = 0, 
            relwidth = 1, 
            relheight = 1
        )

        self.labelTitle = ctk.CTkLabel(
            self.frame_principal, 
            text = "Cristian Garcia Barbershop ", 
            font = ('Montserrat', 25), 
            pady = 40
        )
        self.labelTitle.pack(
            expand = ctk.NO, 
            fill = ctk.BOTH
        )

        self.lablelTitle_2 = ctk.CTkLabel(
            self.frame_principal, 
            text = "Ingresar", 
            font = ('Roboto', 20), 
            pady = 30
        )
        self.lablelTitle_2.pack(
            expand = ctk.NO, 
            fill = ctk.BOTH
        )

    def entrys (self):
        self.usuario = ctk.CTkEntry(
            self.frame_principal, 
            font = ('Roboto', 14), 
            placeholder_text = "Usuario", 
            width = 300
        )
        self.usuario.pack(
            padx = 20, 
            pady = 30, 
            anchor = "center"
        )

        self.contraseña = ctk.CTkEntry(
            self.frame_principal, 
            font = ('Roboto', 14), 
            placeholder_text = "Contraseña", 
            width = 300
        )
        self.contraseña.pack(
            padx = 20, 
            pady = 30, 
            anchor = "center"
        )
        self.contraseña.configure(show = "*")

        self.buttoninicio = ctk.CTkButton(self.frame_principal, text = "Iniciar Sesion", fg_color = 'black', height = 35, command = self.verificar)
        self.buttoninicio.pack(pady = 30)
        self.buttoninicio.bind("<Return>", (lambda event:self.verificar()))
        
        self.mainloop()
=======

        self.root = ctk.CTk()
        self.root.iconbitmap("./imagenes/logo.ico")
        self.root.title('Inicio de Sesion')
        self.root.geometry('800x500')
        w, h = 800, 500

        utl_ventana.centrar_ventana(self.root, w, h)

        logo = utl_imagenes.leer_imagen("./imagenes/logo_login.png", (250, 250))


       #Frame logo
        frame_logo = ctk.CTkFrame(master = self.root, bg_color = '#EEEEEE', width = 450)
        frame_logo.pack(side = "left", expand = ctk.NO, fill = ctk.BOTH)

        label = ctk.CTkLabel(frame_logo, text = "", image = logo, bg_color = '#EEEEEE')
        label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        #Frame principal
        frame_principal = ctk.CTkFrame(master = self.root, border_width = 0, bg_color = 'black', border_color = 'black')
        frame_principal.pack(side = "right", expand = ctk.YES, fill = ctk.BOTH)

        title = ctk.CTkLabel(frame_principal, text = "Cristian Garcia Barbershop ", font = ('Montserrat', 25), pady = 40)
        title.pack(expand = ctk.NO, fill = ctk.BOTH)


        title2 = ctk.CTkLabel(frame_principal, text = "Ingresar", font = ('Roboto', 20), pady = 30)
        title2.pack(expand = ctk.NO, fill = ctk.BOTH)
        

        self.usuario = ctk.CTkEntry(frame_principal, font = ('Roboto', 14), placeholder_text = "Usuario", width = 300)
        self.usuario.pack( padx = 20, pady = 30, anchor = "center")


        self.contraseña = ctk.CTkEntry(frame_principal, font = ('Roboto', 14), placeholder_text = "Contraseña", width = 300)
        self.contraseña.pack(padx = 20, pady = 30, anchor = "center")
        self.contraseña.configure(show = "*")


        inicio = ctk.CTkButton(frame_principal, text = "Iniciar Sesion", fg_color = 'black', height = 35, command = self.verificar)
        inicio.pack(pady = 30)
        inicio.bind("<Return>", (lambda event:self.verificar()))




        self.root.mainloop()
>>>>>>> 95034aaddd30230c0e47fa1add3cf28fdb37b8c8
    