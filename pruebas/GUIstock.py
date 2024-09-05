import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Stock")
root.geometry("600x400")

# Configurar el estilo para agregar bordes
style = ttk.Style()
style.configure("Treeview", 
                background="white",
                foreground="black",
                rowheight=25,
                fieldbackground="white",
                bordercolor="gray", 
                borderwidth=2)

style.map("Treeview", background=[('selected', 'gray85')], foreground=[('selected', 'black')])

# Estilo para los bordes de las columnas
style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

# Crear el Treeview con 4 columnas
tree = ttk.Treeview(root, columns=("ID", "Nombre", "Cantidad", "Precio"), show="headings", style="Treeview")

# Definir los encabezados de las columnas
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Cantidad", text="Cantidad")
tree.heading("Precio", text="Precio")

# Definir el tamaño de las columnas
tree.column("ID", anchor="center", width=50)
tree.column("Nombre", anchor="w", width=200)
tree.column("Cantidad", anchor="center", width=100)
tree.column("Precio", anchor="center", width=100)

# Agregar productos a la tabla
products = [
    ("001", "Shampoo", 50, "$10.00"),
    ("002", "Gel Fijador", 30, "$5.50"),
    ("003", "Aceite para Barba", 20, "$12.00"),
    ("004", "Cera para Cabello", 25, "$8.00"),
    ("005", "Peine", 100, "$2.00")
]

# Insertar cada producto en el Treeview
for product in products:
    tree.insert("", "end", values=product)

# Empaquetar el Treeview en la ventana
tree.pack(expand=True, fill="both")

# Iniciar el loop principal
root.mainloop()

