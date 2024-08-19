import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Configuración de customtkinter
ctk.set_appearance_mode("System")  # "Light", "Dark" or "System"
ctk.set_default_color_theme("blue")  # Tema de colores

# Crear la ventana principal
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gráficas Estadísticas")
        self.geometry("800x600")

        # Frame para los controles
        self.control_frame = ctk.CTkFrame(self)
        self.control_frame.pack(side="left", fill="y", padx=10, pady=10)

        # Frame para la gráfica
        self.graph_frame = ctk.CTkFrame(self)
        self.graph_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Botón para generar el gráfico
        self.plot_button = ctk.CTkButton(self.control_frame, text="Generar Gráfico", command=self.plot_graph)
        self.plot_button.pack(pady=20)

        # Placeholder para el gráfico
        self.canvas = None

    def plot_graph(self):
        # Datos de ejemplo para la gráfica
        x = [1, 2, 3, 4, 5]
        y = [10, 15, 7, 12, 9]

        # Crear la figura de matplotlib
        fig, ax = plt.subplots()
        ax.plot(x, y, marker='o', color='blue', linestyle='-', linewidth=2)
        ax.set_title("Ejemplo de Gráfico de Líneas")
        ax.set_xlabel("Eje X")
        ax.set_ylabel("Eje Y")

        # Eliminar el gráfico anterior si existe
        if self.canvas:
            self.canvas.get_tk_widget().pack_forget()

        # Mostrar la figura en la interfaz de Tkinter
        self.canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

# Crear y ejecutar la aplicación
if __name__ == "__main__":
    app = App()
    app.mainloop()
