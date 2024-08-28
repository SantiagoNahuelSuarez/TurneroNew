import customtkinter as ctk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Controllers.Label_controller import TurnoLabel
from config import *
from util import util_ventana
from .New_customer_window import New_customer_window

class Customer_search_window(ctk.CTkToplevel):
    x = 0
    y = 0
    frame = ctk.CTkFrame
    
    def __init__ (self ,x ,y , frame):
        super().__init__()
        self.config_windows()
        self.x = x
        self.y = y
        self.frame = frame
        self.frames()
        self.buttons_maker()
        self.labels_maker()
        self.inputs_maker()
        
        
        self.grab_set()  # Bloquea la interacción con otras ventanas hasta que se cierre esta
        self.transient(self.frame)  # Mantener la ventana siempre sobre su "master"
        self.lift()  # Llevar la subventana al frente

    def config_windows(self):
        self.title('Cargar Cliente')
        self.iconbitmap("./imagenes/logo.ico")
        w, h = 600, 400
        util_ventana.centrar_ventana(self, w, h)
        
    
   
    def label_maker(self):
        self.turno = TurnoLabel(self.frame, "Paula", "Soria")
        self.turno.place(x=self.x, y=self.y)
        self.destroy()

    def frames(self):
        self.buttonsframe = ctk.CTkFrame(self, height = 150, fg_color= COLOR_MENU_LATERAL)
        self.buttonsframe.pack(side = ctk.BOTTOM, fill = "x", pady = 0)
        
        self.inputframe = ctk.CTkFrame(self, fg_color=COLOR_CUERPO_PRINCIPAL, corner_radius=0 )
        self.inputframe.pack(side = ctk.TOP, expand = True, fill = "both", pady = 0)
    
        self.search_customerframe = ctk.CTkFrame(self.inputframe, fg_color = COLOR_GRIS_PASTEL_FRAMES, height= 100, width=500)
        self.search_customerframe.place(x = 50 ,y= 20)
        self.search_customerframe.pack_propagate(False)
        
        self.serviceframe = ctk.CTkFrame(self.inputframe, fg_color = COLOR_GRIS_PASTEL_FRAMES, height= 160 , width=500)
        self.serviceframe.place(x = 50, y = 150)

    def buttons_maker(self):
        self.btncheck = ctk.CTkButton(self.buttonsframe, height = 30, width = 80, text = "Reservar",
                                      fg_color=COLOR_AZUL_BOTONES)
        self.btncheck.pack(side = ctk.RIGHT, padx = 40, pady = 10, expand = False)
        self.btncheck.bind("<Button-1>", lambda event : self.label_maker())
        
        btnexit = ctk.CTkButton(self.buttonsframe, height = 30, width = 80, text = "Cancelar", fg_color= COLOR_AZUL_BOTONES,
                                command = lambda : self.destroy())
        btnexit.pack(side = ctk.LEFT, padx = 40, pady = 10)
        
        btn_newcustomer = ctk.CTkButton(self.search_customerframe, fg_color = "#BDBDBD",
                                        height = 20, width = 80, text = "Crear nuevo cliente",
                                        text_color=COLOR_GRIS_PASTEL_OSCURO, command= New_customer_window)       
        btn_newcustomer.pack(side = ctk.BOTTOM, anchor = "e", padx = 20, pady = 10)
        
    def inputs_maker(self):
        self.input_name = ctk.CTkEntry(self.search_customerframe,fg_color=COLOR_CUERPO_PRINCIPAL, placeholder_text='numero / nombre / apellido', width=400, height=28)
        self.input_name.place(x = 50, y = 32) 
        
        self.service_choice = ctk.CTkOptionMenu(self.serviceframe,values=['Corte', 'Corte y barba', "Barba Express"],
                                                 width=400, height=28,fg_color=COLOR_CUERPO_PRINCIPAL,text_color=COLOR_GRIS_PASTEL_OSCURO,
                                                 command=self.Service_choice_callback, button_color=COLOR_AZUL_BOTONES,
                                                 dropdown_fg_color= COLOR_CUERPO_PRINCIPAL,dropdown_text_color=COLOR_GRIS_PASTEL_OSCURO,
                                                 variable=ctk.StringVar(value='Elija un servicio :'))
        self.service_choice.place(x=50, y=32)
        
        self.service_cost = ctk.CTkEntry(self.serviceframe, placeholder_text="$ 0", width=400, height=28, fg_color = COLOR_CUERPO_PRINCIPAL, placeholder_text_color=COLOR_GRIS_PASTEL_OSCURO)
        self.service_cost.place (x = 50, y = 102)
           
    def labels_maker(self):
        lbl =  ctk.CTkLabel(self.search_customerframe, text='Cliente: ', width=40, height=28, fg_color='transparent', text_color=COLOR_GRIS_PASTEL_OSCURO)
        lbl.place(x = 50, y = 7)
        
        lblservice =  ctk.CTkLabel(self.serviceframe, text='Servicio: ', width=40, height=28, fg_color='transparent', text_color=COLOR_GRIS_PASTEL_OSCURO)
        lblservice.place(x = 50, y = 7)
        
        lblservicecost =  ctk.CTkLabel(self.serviceframe, text='Precio: ', width=40, height=28, fg_color='transparent', text_color=COLOR_GRIS_PASTEL_OSCURO)
        lblservicecost.place(x = 50, y = 77)

    def Service_choice_callback(self, choice):
        print('optionmenu dropdown clicked:', choice)