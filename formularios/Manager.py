import tkinter as tk
from tkinter import font as tkfont
from enum import Enum
from config import *
import util.util_imagenes as util_img
import util.util_ventana as util_ventana
from formularios.screens import billing_point
from formularios.undefinedscreen import UndefinedScreen

class Side(Enum):
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    LEFT = 3

class ControlLabel(tk.Frame):
    def __init__(self, parent, *args, text="", **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self._inner_label = tk.Label(self, text=text, bg=kwargs.get("bg", ""))
        self._inner_label.pack(fill=tk.BOTH, expand=True)
        self.pack_propagate(0)

        label_font = tkfont.Font(font=self._inner_label["font"])
        text_width = label_font.measure(text)
        text_height = label_font.metrics('linespace')

        self._min_height = max(kwargs.get("height", text_height), text_height)
        self._min_width = max(kwargs.get("width", text_width), text_width)
        self.configure(height=self._min_height, width=self._min_width)

        self.max_side_trigger_dist = 5

        self._start_x = 0
        self._start_y = 0
        self._start_height = 0
        self._start_width = 0
        self._clicked_side = None

        self._inner_label.bind("<Motion>", self.on_mouse_move)
        self._inner_label.bind("<B1-Motion>", self.on_mouse_drag)

    def on_mouse_drag(self, event):
        x = self.winfo_x()
        y = self.winfo_y()
        height = self.winfo_height()

        match self._clicked_side:
            case Side.TOP:
                bottom_left_y = height + y
                height = min(max(self._min_height, height - event.y), bottom_left_y)
                y = bottom_left_y - height
            case Side.BOTTOM:
                height = min(max(self._min_height, event.y), self.parent.winfo_height() - y)
            case _:
                max_x = self.parent.winfo_width() - self._start_width
                max_y = self.parent.winfo_height() - self._start_height
                x = min(max(0, x - self._start_x + event.x), max_x)
                y = min(max(0, y - self._start_y + event.y), max_y)

        self.place(x=x, y=y, height=height)
        
    def on_mouse_move(self, event):
        self._start_x = event.x
        self._start_y = event.y
        self._start_width = self.winfo_width()
        self._start_height = self.winfo_height()

        # Verificar si el click fue en esquinas
        if event.y <= self.max_side_trigger_dist:
            self._clicked_side = Side.TOP
            self.configure(cursor="top_side")

        elif event.y >= self._start_height - self.max_side_trigger_dist:
            self._clicked_side = Side.BOTTOM
            self.configure(cursor="bottom_side")
        else:
            self._clicked_side = None
            self.configure(cursor="hand1")


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
        font_awesome = tkfont.Font(family='FontAwesome', size=12) 
        
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
        font_awesome = tkfont.Font(family='FontAwesome', size=15)
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
        self.control_label = ControlLabel(
            self.principal_body,
            text="Stack Overflow en Español",
            bg="green",
            width=300,
            height=30
            )
        self.control_label.place(x=100, y=100)
    
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