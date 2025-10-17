class Biblioteca:
    def __init__(self, titular: str):
        self._titular = titular
        self.categorias = {
            "Comedia": ["Risas", "Alegría", "Felicidad"],
            "Historia": ["Segunda Guerra", "Grecia", "Socrates"]
        }

    @property
    def titular(self):
        return self._titular

    def usuario(self, nuevo_nombre: str):
        if nuevo_nombre.strip():
            self._titular = nuevo_nombre.strip()

    def agregar_libro(self, categoria: str, libro: str):
        if categoria in self.categorias:
            self.categorias[categoria].append(libro)
        else:
            print(f"La categoría '{categoria}' no existe.")

    def crear_categoria(self, nombre_categoria: str, libros: list):
        nombre_limpio = nombre_categoria.strip().capitalize()
        if nombre_limpio and nombre_limpio not in self.categorias:
            self.categorias[nombre_limpio] = libros
            return True
        return False

    def a_diccionario(self) -> dict:
        return {
            'titular': self.titular,
            'categorias': self.categorias
        }
    
    @classmethod
    def desde_diccionario(cls, datos: dict):
        titular = datos.get('titular', 'Invitado')
        biblioteca = cls(titular)
        biblioteca.categorias = datos.get('categorias', biblioteca.categorias)
        return biblioteca
