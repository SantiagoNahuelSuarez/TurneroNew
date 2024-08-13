from PIL import ImageTk, Image # Este paquete, se utiliza para manejar imagenes png

def leer_imagen(path, size): #Le pasamos la ruta de la imagen en (path(ruta en ingles)) y el tamaño (size) a redimensionar 
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ADAPTIVE)) #reedimensionamos el tamaño de la imagen
