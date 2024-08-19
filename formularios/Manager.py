import customtkinter as ctk
from enum import Enum
from config import *
import util.util_imagenes as util_img
import util.util_ventana as util_ventana
from formularios.screens import billing_point
from formularios.undefinedscreen import UndefinedScreen

ctk.set_appearance_mode("System")  # Opciones: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Opciones: "blue" (default), "green", "dark-blue"

class Side(Enum):
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    LEFT = 3

class ControlLabel(ctk.CTkFrame):
    def __init__(self, parent, *args, text="", **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self._inner_label = ctk.CTkLabel(self, text=text)
        self._inner_label.pack(fill=ctk.BOTH, expand=True)
        self.pack_propagate(0)

        label_font = ctk.CTkFont(font=self._inner_label["font"])
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



class principalscreen(ctk.CTk):
    
    def __init__(self):
        super().__init__() 
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
        self.top_bar = ctk.CTkFrame(
            self,
            fg_color=COLOR_BARRA_SUPERIOR,
            height=50)
        self.top_bar.pack(side=ctk.TOP, fill='both')
        
        self.side_menu = ctk.CTkFrame(
            self,
            fg_color=COLOR_MENU_LATERAL,
            width=150)
        self.side_menu.pack(side=ctk.LEFT, fill='both', expand=False)
        
        self.principal_body = ctk.CTkFrame(
            self,
            fg_color=COLOR_CUERPO_PRINCIPAL)
        self.principal_body.pack(side=ctk.RIGHT, fill='both', expand=True)

    def topbar_controls(self):
        font_awesome = ctk.CTkFont(family='FontAwesome', size=12)
        
        self.labelTitle = ctk.CTkLabel(self.top_bar, text="LABS")
        self.labelTitle.configure(text_color="#fff",
                                  font=("Roboto", 15),
                                  fg_color=COLOR_BARRA_SUPERIOR,
                                  pady=10,
                                  width=16)
        self.labelTitle.pack(side=ctk.LEFT, fill="both")
    
        self.buttonmenu = ctk.CTkButton(self.top_bar,
                                        text="\uf0c9",
                                        font=font_awesome,
                                        fg_color=COLOR_BARRA_SUPERIOR,
                                        text_color="white",
                                        hover_color=None,
                                        width=30)
        self.buttonmenu.pack(side=ctk.LEFT)
        
        self.labelTitle = ctk.CTkLabel(self.top_bar, text="onir.valiente@gmail.com")
        self.labelTitle.configure(text_color="#fff",
                                  font=("Roboto", 10),
                                  fg_color=COLOR_BARRA_SUPERIOR,
                                  padx=10,
                                  width=20)
        self.labelTitle.pack(side=ctk.RIGHT)

    def sidebar_menu_controls(self):
        width_menu = 20
        heigth_menu = 2
        font_awesome = ctk.CTkFont(family='FontAwesome', size=15)
        
        self.labelperfil = ctk.CTkLabel(self.side_menu, image=self.perfil, fg_color=COLOR_MENU_LATERAL)
        self.labelperfil.pack(side=ctk.TOP, pady=10)
        
        self.buttondashboard = ctk.CTkButton(self.side_menu)
        self.buttonbilling = ctk.CTkButton(self.side_menu)
        self.buttonemployeds = ctk.CTkButton(self.side_menu)
        self.buttoncustomers = ctk.CTkButton(self.side_menu)
        self.buttonstock = ctk.CTkButton(self.side_menu)
        self.buttonsettings = ctk.CTkButton(self.side_menu)

        buttons_info = [
            ("Dashboard", "\uf109", self.buttondashboard),
            ("Punto de Venta", "\uf015", self.buttonbilling),
            ("Empleados", "\uf007", self.buttonemployeds),
            ("Clientes", "\uf007", self.buttoncustomers),
            ("Stock", "\uf129", self.buttonstock),
            ("Configuración", "\uf013", self.buttonsettings)
        ]



