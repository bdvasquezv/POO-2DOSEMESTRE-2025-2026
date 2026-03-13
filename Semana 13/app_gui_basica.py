import tkinter as tk
from tkinter import messagebox

# Clase principal que define la aplicación GUI
class SimpleGUIApp:
    def __init__(self, root):
        # Configuración de la ventana principal
        self.root = root
        self.root.title("Gestor de Información - Aplicación GUI")
        self.root.geometry("400x300")

        # Etiqueta que indica al usuario qué debe hacer
        self.label = tk.Label(root, text="Ingrese información:")
        self.label.pack(pady=10)

        # Campo de texto donde el usuario escribe la información
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        # Botón que permite agregar la información escrita a la lista
        self.add_button = tk.Button(root, text="Agregar", command=self.add_item)
        self.add_button.pack(pady=5)

        # Botón que permite limpiar todos los elementos de la lista
        self.clear_button = tk.Button(root, text="Limpiar", command=self.clear_list)
        self.clear_button.pack(pady=5)

        # Lista donde se mostrarán los datos agregados por el usuario
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

    # Función que se ejecuta cuando el usuario presiona el botón "Agregar"
    def add_item(self):
        item = self.entry.get()  # Obtener el texto ingresado por el usuario

        if item:
            # Insertar el texto en la lista
            self.listbox.insert(tk.END, item)

            # Limpiar el campo de texto después de agregar el elemento
            self.entry.delete(0, tk.END)
        else:
            # Mostrar una advertencia si el campo está vacío
            messagebox.showwarning("Advertencia", "El campo de texto está vacío")

    # Función que limpia todos los elementos de la lista
    def clear_list(self):
        self.listbox.delete(0, tk.END)

# Punto de entrada del programa
if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal
    app = SimpleGUIApp(root)  # Crear la aplicación
    root.mainloop()  # Ejecutar la interfaz gráfica