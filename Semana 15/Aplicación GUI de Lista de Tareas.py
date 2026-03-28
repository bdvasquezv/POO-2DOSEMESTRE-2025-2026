import tkinter as tk
from tkinter import messagebox

# Función para añadir tarea
def add_task():
    task = entry_task.get().strip()  # Elimina espacios innecesarios
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

# Función para marcar tarea como completada
def mark_completed():
    try:
        selected_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_index)

        # Evita duplicar el símbolo ✔
        if not task.startswith("✔ "):
            listbox_tasks.delete(selected_index)
            listbox_tasks.insert(selected_index, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

# Función para eliminar tarea
def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

# Evento al presionar Enter
def on_enter(event):
    add_task()

# Evento doble clic para completar tarea (extra)
def on_double_click(event):
    mark_completed()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Campo de entrada
entry_task = tk.Entry(root, width=40, bg="#ffffff", fg="#000000")
entry_task.pack(pady=10)
entry_task.bind("<Return>", on_enter)

# Botones
frame_buttons = tk.Frame(root, bg="#f0f0f0")
frame_buttons.pack()

btn_add = tk.Button(frame_buttons, text="Añadir Tarea", command=add_task, bg="#4caf50", fg="white")
btn_add.pack(side=tk.LEFT, padx=5)

btn_complete = tk.Button(frame_buttons, text="Marcar como Completada", command=mark_completed, bg="#2196f3", fg="white")
btn_complete.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(frame_buttons, text="Eliminar Tarea", command=delete_task, bg="#f44336", fg="white")
btn_delete.pack(side=tk.LEFT, padx=5)

# Lista de tareas
listbox_tasks = tk.Listbox(
    root,
    width=50,
    height=15,
    bg="#ffffff",
    fg="#000000",
    selectbackground="#c0c0c0"
)
listbox_tasks.pack(pady=10)

# Evento doble clic en la lista
listbox_tasks.bind("<Double-Button-1>", on_double_click)

# Bucle principal
root.mainloop()