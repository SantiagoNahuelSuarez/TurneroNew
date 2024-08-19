import customtkinter as ctk
from PIL import Image

# Configuración básica de customtkinter
ctk.set_appearance_mode("dark")  # Modos: "System", "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Temas: "blue", "dark-blue", "green"

# Crear la ventana principal
root = ctk.CTk()
root.title("Login")
root.geometry("700x400")

# Cargar la imagen
image = ctk.CTkImage(Image.open("./imagenes/logo_login.png"), size=(200, 200))

# Frame principal
frame = ctk.CTkFrame(root, corner_radius=20)  # Bordes redondeados
frame.pack(pady=40, padx=40, fill="both", expand=True)

# Crear un grid de 1 fila y 2 columnas
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=2)

# Colocar la imagen a la izquierda
image_label = ctk.CTkLabel(frame, image=image, text="")
image_label.grid(row=0, column=0, rowspan=4, padx=20, pady=20, sticky="nsew")

# Título del login con fuente personalizada
title_font = ctk.CTkFont(family="Helvetica", size=26, weight="bold")
title_label = ctk.CTkLabel(frame, text="Iniciar Sesión", font=title_font)
title_label.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="w")

# Campo de entrada para el usuario
username_entry = ctk.CTkEntry(frame, placeholder_text="Usuario", height=40, corner_radius=10)
username_entry.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

# Campo de entrada para la contraseña
password_entry = ctk.CTkEntry(frame, placeholder_text="Contraseña", show="*", height=40, corner_radius=10)
password_entry.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

# Botón de login
login_button = ctk.CTkButton(frame, text="Login", height=40, corner_radius=10, fg_color="#1f6aa5")
login_button.grid(row=3, column=1, padx=20, pady=(20, 10), sticky="ew")

# Agregar una etiqueta de texto para "¿Olvidaste tu contraseña?"
forgot_password_label = ctk.CTkLabel(frame, text="¿Olvidaste tu contraseña?", text_color="#1f6aa5", cursor="hand2")
forgot_password_label.grid(row=4, column=1, padx=20, pady=10, sticky="e")

# Ejecutar la aplicación
root.mainloop()


