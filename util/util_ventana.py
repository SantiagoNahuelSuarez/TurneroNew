# determinamos el tamaño de la ventana
def centrar_ventana(window, width_application, height_application):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x = int((screen_width/2) - (screen_width/2))
    y = int((screen_height/2) - (screen_height/2))

    return window.geometry(f"{width_application}x{height_application}+{x}+{y}")