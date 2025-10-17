from app.data.firebase import FirebaseService
from app.presentation.viewmodel import ControladorApp
from app.ui.interfaz import InterfazUsuario

def main():
    firebase = FirebaseService()
    if firebase.ref:
        controlador = ControladorApp(firebase)
        ui = InterfazUsuario(controlador)
        ui.iniciar()
    else:
        print("\n La aplicación no puede iniciar sin una conexión a la base de datos.")

if __name__ == "__main__":
    main()
