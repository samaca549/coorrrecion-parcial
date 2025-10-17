import os
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv

class FirebaseService:
    def __init__(self):
        self.ref = self._conectar()

    def _conectar(self):
        try:
            load_dotenv()
            cred_path = "serviceAccountKey.json"
            database_url = os.getenv("FIREBASE_DATABASE_URL")
            if not os.path.exists(cred_path) or not database_url:
                print(" Error: Asegúrate de tener 'serviceAccountKey.json' y un archivo '.env' con la URL.")
                return None
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred, {'databaseURL': database_url})
            print(" Conexión con Firebase establecida con éxito.")
            return db.reference('biblioteca')
        except ValueError:
            print(" Firebase ya estaba inicializado. Reutilizando conexión.")
            return db.reference('biblioteca')
        except Exception as e:
            print(f" Error crítico al conectar con Firebase: {e}")
            return None

    def guardar_datos(self, datos: dict):
        if self.ref:
            self.ref.set(datos)
            print(" Datos guardados en Firebase con éxito.")
        else:
            print(" No se pueden guardar los datos. No hay conexión a Firebase.")

    def cargar_datos(self) -> dict:
        if self.ref:
            datos_cargados = self.ref.get()
            return datos_cargados if datos_cargados else {}
        else:
            print(" No se pueden cargar los datos. No hay conexión a Firebase.")
            return {}
