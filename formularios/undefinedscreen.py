import tkinter as tk
from config import COLOR_CUERPO_PRINCIPAL


class UndefinedScreen():

    def __init__(self, principal_body, logo):
        self.top_bar = tk.Frame(principal_body)
        self.top_bar.pack(side=tk.TOP, fill=tk.X, expand=False)

        self.bottom_bar = tk.Frame (principal_body)
        self.bottom_bar.pack(side = tk.BOTTOM, fill = "both", expand = True)

        self.top_label = tk.Label(self.top_bar,
                                  text = "Pagina en desarrollo",
                                  fg = "#222d33",
                                  font = ("Roboto", 30),
                                  bg = COLOR_CUERPO_PRINCIPAL, 
                                  pady=20) 
        self.top_label.pack(side = tk.TOP,
                            fill = "both",
                            expand=True ,)

        self.label_image = tk.Label(self.bottom_bar, image=logo)
        self.label_image.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.label_image.config(fg = "#fff", font= ("Roboto", 10), bg = COLOR_CUERPO_PRINCIPAL)