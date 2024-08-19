import customtkinter as ctk

# Función para mostrar/ocultar la contraseña
def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.configure(show="")
        toggle_button.configure(text="Ocultar")
    else:
        password_entry.configure(show="*")
        toggle_button.configure(text="Mostrar")

# Crear la ventana principal
root = ctk.CTk()
root.geometry("300x200")

# Crear un campo de entrada para la contraseña
password_entry = ctk.CTkEntry(root, show="*", placeholder_text="Contraseña")
password_entry.pack(pady=20)

# Crear un botón para mostrar/ocultar la contraseña
toggle_button = ctk.CTkButton(root, text="Mostrar", command=toggle_password)
toggle_button.pack(pady=10)

root.mainloop()
