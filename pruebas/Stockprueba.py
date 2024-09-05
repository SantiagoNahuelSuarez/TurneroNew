import tkinter as tk
from ttkwidgets import Table

root = tk.Tk()
root.geometry("400x300")

# Crear la tabla con columnas
table = Table(root, columns=("ID", "Nombre", "Cantidad", "Precio"), show="headings")
table.heading("ID", text="ID")
table.heading("Nombre", text="Nombre")
table.heading("Cantidad", text="Cantidad")
table.heading("Precio", text="Precio")

# Insertar filas de ejemplo
table.insert("", "end", values=("001", "Shampoo", "50", "$10.00"))
table.insert("", "end", values=("002", "Gel Fijador", "30", "$5.50"))

table.pack(expand=True, fill="both")

root.mainloop()