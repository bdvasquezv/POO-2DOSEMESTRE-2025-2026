import os

class Dashboard:
    def __init__(self, ruta_base):
        self.ruta_base = ruta_base

    def mostrar_semanas(self):
        print("\nSemanas del semestre:")
        for carpeta in os.listdir(self.ruta_base):
            if carpeta.startswith("Semana"):
                print(f"- {carpeta}")

    def crear_semana(self, nombre):
        ruta = os.path.join(self.ruta_base, nombre)
        if not os.path.exists(ruta):
            os.mkdir(ruta)
            print("Semana creada correctamente")
        else:
            print("La semana ya existe")

    def mostrar_tareas(self, semana):
        ruta = os.path.join(self.ruta_base, semana)
        if os.path.exists(ruta):
            print(f"\nTareas de {semana}:")
            for archivo in os.listdir(ruta):
                print(f"- {archivo}")
        else:
            print("La semana no existe")

    def crear_tarea(self, semana, nombre_tarea):
        ruta_semana = os.path.join(self.ruta_base, semana)
        if os.path.exists(ruta_semana):
            ruta_archivo = os.path.join(ruta_semana, nombre_tarea)
            with open(ruta_archivo, "w") as f:
                f.write("# Tarea de Programación Orientada a Objetos\n")
            print("Tarea creada correctamente")
        else:
            print("La semana no existe")


if __name__ == "__main__":
    dashboard = Dashboard(os.getcwd())

    while True:
        print("\n--- DASHBOARD POO ---")
        print("1. Ver semanas")
        print("2. Crear semana")
        print("3. Ver tareas de una semana")
        print("4. Crear tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            dashboard.mostrar_semanas()
        elif opcion == "2":
            nombre = input("Nombre de la semana (Ej: Semana_01): ")
            dashboard.crear_semana(nombre)
        elif opcion == "3":
            semana = input("Nombre de la semana: ")
            dashboard.mostrar_tareas(semana)
        elif opcion == "4":
            semana = input("Nombre de la semana: ")
            tarea = input("Nombre del archivo (Ej: tarea1.py): ")
            dashboard.crear_tarea(semana, tarea)
        elif opcion == "5":
            break
        else:
            print("Opción incorrecta")
