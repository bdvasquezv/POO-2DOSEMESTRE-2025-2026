import os


class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre},{self.cantidad},{self.precio}"


class Inventario:
    ARCHIVO = "inventario.txt"

    def __init__(self):
        self.productos = []
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        # Si el archivo no existe, lo crea automáticamente
        if not os.path.exists(self.ARCHIVO):
            try:
                open(self.ARCHIVO, "w").close()
                print("Archivo de inventario creado correctamente.")
            except PermissionError:
                print("Error: No tienes permisos para crear el archivo.")
            return

        # Intentar leer el archivo
        try:
            with open(self.ARCHIVO, "r") as archivo:
                for linea in archivo:
                    try:
                        nombre, cantidad, precio = linea.strip().split(",")
                        self.productos.append(
                            Producto(nombre, int(cantidad), float(precio))
                        )
                    except ValueError:
                        print("Error: Línea con formato incorrecto en el archivo.")
            print("Inventario cargado correctamente desde el archivo.")
        except FileNotFoundError:
            print("Archivo no encontrado.")
        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")

    def guardar_en_archivo(self):
        try:
            with open(self.ARCHIVO, "w") as archivo:
                for producto in self.productos:
                    archivo.write(str(producto) + "\n")
            print("Archivo actualizado correctamente.")
        except PermissionError:
            print("Error: No se pudo escribir en el archivo. Verifica los permisos.")

    def agregar_producto(self, nombre, cantidad, precio):
        self.productos.append(Producto(nombre, cantidad, precio))
        self.guardar_en_archivo()
        print(f"Producto '{nombre}' agregado correctamente.")

    def actualizar_producto(self, nombre, nueva_cantidad, nuevo_precio):
        for producto in self.productos:
            if producto.nombre == nombre:
                producto.cantidad = nueva_cantidad
                producto.precio = nuevo_precio
                self.guardar_en_archivo()
                print(f"Producto '{nombre}' actualizado correctamente.")
                return
        print("Producto no encontrado.")

    def eliminar_producto(self, nombre):
        producto_encontrado = False
        for producto in self.productos:
            if producto.nombre == nombre:
                self.productos.remove(producto)
                producto_encontrado = True
                break

        if producto_encontrado:
            self.guardar_en_archivo()
            print(f"Producto '{nombre}' eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
            return

        print("Inventario Actual:")
        for producto in self.productos:
            print(f"{producto.nombre} - Cantidad: {producto.cantidad}, Precio: ${producto.precio}")


# Programa principal
if __name__ == "__main__":
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Agregar Producto")
        print("2. Actualizar Producto")
        print("3. Eliminar Producto")
        print("4. Mostrar Inventario")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(nombre, cantidad, precio)

        elif opcion == "2":
            nombre = input("Nombre del producto a actualizar: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(nombre, cantidad, precio)

        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)

        elif opcion == "4":
            inventario.mostrar_inventario()

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intenta de nuevo.")