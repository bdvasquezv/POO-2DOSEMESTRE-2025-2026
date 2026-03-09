# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla inmutable para titulo y autor
        self.titulo_autor = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo_autor[0]} por {self.titulo_autor[1]} (ISBN: {self.isbn}, Categoría: {self.categoria})"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista para almacenar los libros prestados
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        # Diccionario para libros (ISBN -> Libro)
        self.libros = {}

        # Diccionario para usuarios (ID -> Usuario)
        self.usuarios = {}

        # Conjunto para asegurar IDs únicos
        self.ids_usuarios = set()

    # Agregar libro a la biblioteca
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print("Libro agregado correctamente.")
        else:
            print("El libro ya existe en la biblioteca.")

    # Quitar libro
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("El libro no existe.")

    # Registrar usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado correctamente.")
        else:
            print("El ID de usuario ya existe.")

    # Dar de baja usuario
    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # Prestar libro
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros.pop(isbn)

            usuario.libros_prestados.append(libro)

            print(f"Libro prestado a {usuario.nombre}")
        else:
            print("Usuario o libro no encontrado.")

    # Devolver libro
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]

            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    print("Libro devuelto correctamente.")
                    return

            print("El usuario no tiene ese libro.")
        else:
            print("Usuario no encontrado.")

    # Buscar libro por titulo, autor o categoria
    def buscar_libro(self, criterio, valor):
        encontrados = []

        for libro in self.libros.values():

            if criterio == "titulo" and libro.titulo_autor[0].lower() == valor.lower():
                encontrados.append(libro)

            elif criterio == "autor" and libro.titulo_autor[1].lower() == valor.lower():
                encontrados.append(libro)

            elif criterio == "categoria" and libro.categoria.lower() == valor.lower():
                encontrados.append(libro)

        if encontrados:
            print("Libros encontrados:")
            for libro in encontrados:
                print(libro)
        else:
            print("No se encontraron libros.")


    # Listar libros prestados de un usuario
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]

            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("El usuario no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


# Menú del sistema
def menu():

    biblioteca = Biblioteca()

    while True:

        print("\n--- Sistema  de Biblioteca Digital ---")
        print("1. Agregar libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")

            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            isbn = input("ISBN del libro: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")

            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            id_usuario = input("ID del usuario: ")
            biblioteca.dar_de_baja_usuario(id_usuario)

        elif opcion == "5":
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")

            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "6":
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")

            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "7":
            criterio = input("Buscar por (titulo, autor, categoria): ")
            valor = input("Valor: ")

            biblioteca.buscar_libro(criterio, valor)

        elif opcion == "8":
            id_usuario = input("ID del usuario: ")
            biblioteca.listar_libros_prestados(id_usuario)

        elif opcion == "9":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


# Ejecutar programa
if __name__ == "__main__":
    menu()