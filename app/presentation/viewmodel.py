from app.domain.Biblioteca import Biblioteca
from app.data.firebase import FirebaseService

class ControladorApp:
    def __init__(self, firebase_service: FirebaseService):
        self.firebase = firebase_service
        self.cargar_o_registrar_usuario()

    def cargar_o_registrar_usuario(self):
        datos = self.firebase.cargar_datos()

        if not datos or "titular" not in datos:
            nombre = input(" Ingresa tu nombre para registrar tu biblioteca: ").strip()
            if not nombre:
                nombre = "Invitado"
            self.biblioteca = Biblioteca(nombre)
            self.firebase.guardar_datos(self.biblioteca.a_diccionario())
            print(f" Biblioteca registrada a nombre de {nombre}.")
        else:
            self.biblioteca = Biblioteca.desde_diccionario(datos)
            print(f" ¡Bienvenido de nuevo, {self.biblioteca.titular}!")

    def guardar_y_salir(self):
        datos_para_guardar = self.biblioteca.a_diccionario()
        self.firebase.guardar_datos(datos_para_guardar)
        print(f" ¡Hasta luego, {self.biblioteca.titular}!")

    def obtener_datos_para_mostrar(self) -> dict:
        return self.biblioteca.categorias

    def agregar_libro(self, categoria, libro):
        self.biblioteca.agregar_libro(categoria, libro)

    def crear_nueva_categoria(self, nombre_categoria, libros_str):
        libros_lista = [libro.strip() for libro in libros_str.split(',')]
        if self.biblioteca.crear_categoria(nombre_categoria, libros_lista):
            print(f" Categoría '{nombre_categoria.capitalize()}' creada con éxito.")
        else:
            print(" No se pudo crear la categoría. ¿Ya existe o el nombre está vacío?")
