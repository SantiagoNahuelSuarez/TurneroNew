def centrar_ventana(ventana,ancho_ventana, alto_ventana ):
    ventana.update_idletasks()
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    x = (ancho_pantalla // 2) - (ancho_ventana // 2) + 100
    y = (alto_pantalla // 2) - (alto_ventana // 2) + 45
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")