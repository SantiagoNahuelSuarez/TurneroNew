#Ventana de Login

from tkinter import messagebox
import customtkinter as ctk
import os
from PIL import ImageTk, Image
import util.util_imagenes as utl_imagenes
import util.util_ventana as utl_ventana
from formularios.Manager import principalscreen

carpeta_principal = os.path.dirname(__file__)

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue") 

class app: 

    def verificar(self):

        user = self.usuario.get()
        password = self.contraseña.get()

        if(user == 'Root' and password == "1234"):
            self.root.destroy()
            principalscreen()
        else:
            messagebox.showerror(message = "La contraseña no es correcta", title = "Mensaje")

    def __init__(self):

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
    