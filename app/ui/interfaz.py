from app.presentation.viewmodel import ControladorApp

class InterfazUsuario:
    def __init__(self, controlador: ControladorApp):
        self.controlador = controlador

    def iniciar(self):
        print(f"\n ¡Bienvenido, {self.controlador.biblioteca.titular}!")
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ").strip()

            if opcion == '1':
                self.mostrar_libros()
            elif opcion == '2':
                self.crear_categoria()
            elif opcion == '3':
                self.usuario()
            elif opcion == '4':
                self.controlador.guardar_y_salir()
                break
            else:
                print(" Opción no válida.")

    def mostrar_menu(self):
        print("\n--- MENÚ DE LA BIBLIOTECA ---")
        print("1. Mostrar todos los libros por categoría")
        print("2. Crear una nueva categoría de libros")
        print("3. agregar usuario")
        print("4. Guardar y salir")
        print("-------------------------------")

    def mostrar_libros(self):
        catalogo = self.controlador.obtener_datos_para_mostrar()
        print("\n---  Tu Catálogo de Libros ---")
        if not catalogo:
            print("No hay categorías definidas.")
        else:
            for categoria, libros in catalogo.items():
                print(f"\n>> Categoría: {categoria}")
                for i, libro in enumerate(libros, 1):
                    print(f"   {i}. {libro}")
        print("-" * 30)

    def crear_categoria(self):
        print("\n--- Nueva Categoría ---")
        nombre = input("Nombre de la nueva categoría: ")
        libros = input("Escribe los libros separados por comas: ")
        self.controlador.crear_nueva_categoria(nombre, libros)

    def usuario(self):
        nuevo_nombre = input("\n Ingresa el nuevo nombre del titular: ").strip()
        if nuevo_nombre:
            self.controlador.biblioteca.usuario(nuevo_nombre)
            self.controlador.firebase.guardar_datos(self.controlador.biblioteca.a_diccionario())
            print(f"Titular actualizado a '{nuevo_nombre}'.")
        else:
            print(" No se ingresó ningún nombre.")
