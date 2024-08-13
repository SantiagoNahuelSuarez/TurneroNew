# aca hacemos todo el diseño
import tkinter as tk
from tkinter import font
from config import *
import util.util_imagenes as util_img
import util.util_ventana as util_ventana
from formularios.screens import billing_point
from formularios.undefinedscreen import UndefinedScreen


class principalscreen(tk.Tk):
    
    def __init__(self) :
        super().__init__() # inicializamos el objeto
        self.logo = util_img.leer_imagen("./imagenes/logo.png", (560,136))
        self.perfil = util_img.leer_imagen("./imagenes/perfil.png", (100,100))
        self.fondo = util_img.leer_imagen("./imagenes/fondo.png", (984,603))
        self.config_window()
        self.frames()
        self.topbar_controls()
        self.sidebar_menu_controls()
        self.principal_body_controls()

    def config_window(self):
        self.title('LABS')
        self.iconbitmap("./imagenes/logo.ico")
        w, h = 1024, 600
        util_ventana.centrar_ventana(self, w, h)
        
    def frames(self):
        self.top_bar = tk.Frame(
            self,
            bg = COLOR_BARRA_SUPERIOR, 
            height = 50 )
        self.top_bar.pack(
                side=tk.TOP,
                fill = 'both'
            )
        
        self.side_menu = tk.Frame(
            self,
            bg = COLOR_MENU_LATERAL, 
            width = 150 )
        self.side_menu.pack(
                side=tk.LEFT,
                fill = 'both',
                expand = False
            )
        
        self.principal_body = tk.Frame(
            self,
            bg = COLOR_CUERPO_PRINCIPAL
            )
        self.principal_body.pack(
                side=tk.RIGHT,
                fill = 'both',
                expand = True
            )

    def topbar_controls (self):
        font_awesome = font.Font(family='FontAwesome', size=12) 
        
        self.labelTitle = tk.Label(self.top_bar, text="LABS")
        self.labelTitle.config(fg = "#fff", 
                            font = ("Roboto", 15),
                                bg = COLOR_BARRA_SUPERIOR,
                                pady = 10,
                                width = 16 )
        self.labelTitle.pack(side = tk.LEFT,fill = "both")
    
        self.buttonmenu = tk.Button (self.top_bar,
                                    text="\uf0c9",
                                    font = font_awesome,
                                    bd = 0,    
                                    bg = COLOR_BARRA_SUPERIOR,
                                    fg = "white")
        self.buttonmenu.pack(side = tk.LEFT) 
        
        
        
        self.labelTitle = tk.Label(self.top_bar, text="onir.valiente@gmail.com")
        self.labelTitle.config(fg = "#fff", 
                            font = ("Roboto", 10),
                                bg = COLOR_BARRA_SUPERIOR,
                                padx = 10,
                                width = 20 )
        self.labelTitle.pack(side = tk.RIGHT)

    def sidebar_menu_controls (self):
        width_menu = 20
        heigth_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
        #imagenes como etiquetas
        self.labelperfil = tk.Label(
            self.side_menu, 
            image = self.perfil,    #Self.perfil, constante definida en el manager
            bg = COLOR_MENU_LATERAL)
        self.labelperfil.pack(side = tk.TOP,
                            pady = 10)
        
        #buttos for the menu
        self.buttondashboard = tk.Button(self.side_menu)
        self.buttonbilling = tk.Button(self.side_menu)
        self.buttonemployeds = tk.Button(self.side_menu)
        self.buttoncustomers = tk.Button(self.side_menu)
        self.buttonstock = tk.Button(self.side_menu)
        self.buttonsettings = tk.Button(self.side_menu)

        buttons_info = [
            ("Dashboard", "\uf109", self.buttondashboard,self.principal_body_controls),
            ("Punto de Venta", "\uf015", self.buttonbilling,self.show_undefinedscreen),
            ("Empleados", "\uf007", self.buttonemployeds, self.show_undefinedscreen),
            ("Clientes", "\uf007", self.buttoncustomers, self.show_undefinedscreen),
            ("Stock", "\uf129", self.buttonstock, self.show_undefinedscreen),
            ("Configuracion", "\uf013", self.buttonsettings, self.show_undefinedscreen)
        ]

        for text, icon, button, cmd in buttons_info:
            self.config_button_menu(button, text, icon, font_awesome, width_menu, heigth_menu, cmd)

    def principal_body_controls(self):
        self.screen_cleaner(self.principal_body)
        self.label = tk.Label(self.principal_body, bg="green", width=30, height=3)
        self.label.place(x=0, y=0)

        def arrastrar(event):
            self.label.startX = event.x
            self.label.startY = event.y

        def arrastrar2(event):
            x = self.label.winfo_x() - self.label.startX + event.x
            y = self.label.winfo_y() - self.label.startY + event.y

            # Obtiene las dimensiones del frame principal
            frame_width = self.principal_body.winfo_width()
            frame_height = self.principal_body.winfo_height()
            
            # Obtiene las dimensiones del widget
            widget_width = self.label.winfo_width()
            widget_height = self.label.winfo_height()

            # Limita el movimiento dentro del frame
            if 0 <= x <= frame_width - widget_width and 0 <= y <= frame_height - widget_height:
                self.label.place(x=x, y=y)

        def clic(event):
            # Almacena la posición inicial del clic y el tamaño inicial del widget
            self.label.startX = event.x
            self.label.startY = event.y
            self.label.startY_root = event.y_root
            self.initial_width = self.label.winfo_width()
            self.initial_height = self.label.winfo_height()
            
        def resize(event):
            # Obtiene la posición actual del ratón
            current_y = event.y_root

            # Calcula el cambio en la altura
            delta_y = current_y - self.label.startY_root

            # Calcula la nueva altura
            new_height = max(self.initial_height + delta_y - self.label.startY, 10)

            # Actualiza la altura del label
            self.label.configure(height=new_height)

            # Actualiza la posición inicial del ratón
            self.label.startY_root = current_y


                
        
        self.label.bind("<Button-1>", arrastrar)
        self.label.bind("<B1-Motion>", arrastrar2)

        # Agrega el evento de redimensionamiento a los bordes de la etiqueta
        self.label.bind("<Button-1>",  clic)
        self.label.bind("<B1-Motion>", resize, add="+")
    
    def config_button_menu(self, button, text, icon, font_awesome, width_menu, height_menu, cmd):

            button.config(text = f"  {icon}   {text}",
                        anchor = "w",
                        font = font_awesome,
                        bd = 0,
                        bg = COLOR_MENU_LATERAL,
                        fg = "white",
                        width = width_menu,
                        height= height_menu,
                        command = cmd)
            button.pack(side = tk.TOP)    
            self.bind_hover_events(button)

    def bind_hover_events (self, button):
        button.bind("<Enter>", lambda event:  self.on_enter(event, button))
        button.bind("<Leave>", lambda event:  self.on_leave(event, button))

    def on_enter(self,event, button): # aca indicamos cuando tenemos el mouse encima de que color cambia
        button.config (bg = COLOR_MENU_CURSOR_ENCIMA, fg = "white")

    def on_leave(self, event, button):# aca indicamos cuando tenemos el mouse no esta encima que se mantenga del mismo color
        button.config (bg = COLOR_MENU_LATERAL, fg = "white")
    # Bind es una propiedad de cada widget para asociar un evento cuanto esta el cursor encima
    def show_screen(self):
        billing_point()

    def show_undefinedscreen(self):
       self.screen_cleaner(self.principal_body)
       UndefinedScreen(self.principal_body, self.fondo)

    def screen_cleaner(self, screen):
        for widget in screen.winfo_children(): # esta funcion es para determinar todos los widgets de un frame o ventana
            widget.destroy() # con esto destruimos el widget