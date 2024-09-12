import customtkinter as ctk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import *
from util import util_ventana

class New_empleado_window(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.config_windows()
        self.title("Agregar Empleado")
        self.frames()
        self.labels_maker()
        self.buttons_maker()
        self.inputs_maker()
        
        self.grab_set()  # Bloquea la interacción con otras ventanas hasta que se cierre esta
        self.lift()  # Llevar la subventana al frente

    def config_windows(self):
        self.iconbitmap("./imagenes/logo.ico")
        w, h = 400, 400
        util_ventana.centrar_ventana(self, w, h)
        
    def frames(self):
        self.buttonsframe = ctk.CTkFrame(self, height = 150, fg_color= COLOR_MENU_LATERAL)
        self.buttonsframe.pack(side = ctk.BOTTOM, fill = "x", pady = 0)
        
        self.inputframe = ctk.CTkFrame(self, fg_color=COLOR_CUERPO_PRINCIPAL )
        self.inputframe.pack(side = ctk.TOP, expand = True, fill = "both", pady = 0)
    
        self.search_customerframe = ctk.CTkFrame(self.inputframe, fg_color = COLOR_GRIS_PASTEL_FRAMES, height= 310, width=300)
        self.search_customerframe.place(x = 50 ,y= 20)
        self.search_customerframe.pack_propagate(False)
        

    def buttons_maker(self):
        self.btncheck = ctk.CTkButton(self.buttonsframe, height = 30, width = 80, text = "Agregar",
                                      fg_color=COLOR_AZUL_BOTONES)
        self.btncheck.pack(side = ctk.RIGHT, padx = 40, pady = 10, expand = False)
        self.btncheck.bind("<Button-1>", lambda event : print("pass"))
        
        btnexit = ctk.CTkButton(self.buttonsframe, height = 30, width = 80, text = "Cancelar", fg_color= COLOR_AZUL_BOTONES,
                                command = lambda : self.destroy())
        btnexit.pack(side = ctk.LEFT, padx = 40, pady = 10)
        
    def inputs_maker(self):
        self.input_ID = ctk.CTkEntry(self.search_customerframe,fg_color=COLOR_CUERPO_PRINCIPAL,
                                       placeholder_text='*Obligatorio*', width=200, height=28)
        self.input_ID.place(x = 50, y = 78) 
        
        self.input_name = ctk.CTkEntry(self.search_customerframe,fg_color=COLOR_CUERPO_PRINCIPAL,
                                       placeholder_text='*Obligatorio*', width=200, height=28)
        self.input_name.place(x = 50, y = 136) 
        
        self.input_surname = ctk.CTkEntry(self.search_customerframe,fg_color=COLOR_CUERPO_PRINCIPAL,
                                       placeholder_text='*Obligatorio*', width=200, height=28)
        self.input_surname.place(x = 50, y = 194) 
        
           
    def labels_maker(self):
        lblgral =  ctk.CTkLabel(self.search_customerframe, text='Datos del nuevo Empleado: ',
                                width=40, height=28, fg_color='transparent', text_color=COLOR_GRIS_PASTEL_OSCURO)
        lblgral.place(x = 30, y = 18)
        
        lblnoID =  ctk.CTkLabel(self.search_customerframe, text='Id : ', width=40, height=28,
                                  fg_color='transparent', text_color=COLOR_GRIS_PASTEL_OSCURO)
        lblnoID.place(x = 50, y = 50)
        
        lblname =  ctk.CTkLabel(self.search_customerframe, text='Nombre : ', width=40, height=28,
                                  fg_color='transparent', text_color=COLOR_GRIS_PASTEL_OSCURO)
        lblname.place(x = 50, y = 108)
        
        lblsurname =  ctk.CTkLabel(self.search_customerframe, text='Apellido : ', width=40, height=28,
                                  fg_color='transparent', text_color=COLOR_GRIS_PASTEL_OSCURO)
        lblsurname.place(x = 50, y = 166)
        
        
