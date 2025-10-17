<img width="439" height="617" alt="{961492B1-49D9-4D9C-9166-597F9F0E8BC9}" src="https://github.com/user-attachments/assets/64d21d02-4e38-4608-89b2-ef02d199674a" />
Este código representa una biblioteca sencilla donde cada persona puede tener su propio espacio con categorías de libros. Al iniciar, se asigna un titular  y se crean algunas categorías básicas como Comedia e Historia. Luego, el programa permite cambiar el nombre del titular, agregar nuevos libros, crear categorías nuevas y guardar toda la información en forma de diccionario. Esto facilita que los datos puedan almacenarse o recuperarse fácilmente desde una base de datos, como Firebase. En resumen, el código organiza y gestiona una pequeña biblioteca personal de manera práctica y clara.
CORRECCIONES
El código original presentaba varios problemas de estructura y repetición. Se mezclaban demasiadas tareas dentro de una sola clase, lo que dificultaba su lectura y mantenimiento. Además, el manejo de categorías y libros era poco eficiente, ya que se usaban muchas listas separadas en lugar de estructuras más organizadas. También había errores de validación al pedir datos por consola y faltaba una forma clara de guardar o recuperar la información. Las versiones corregidas solucionaron esto dividiendo las responsabilidades: se creó una clase Biblioteca más ordenada, que maneja categorías y libros de forma dinámica, y se agregaron conexiones con Firebase para guardar los datos en línea. En general, la corrección hizo el código más limpio, reutilizable y fácil de entender.
<img width="1519" height="494" alt="{09015530-7A3B-4306-A943-E21A48D10EC2}" src="https://github.com/user-attachments/assets/d394208d-258e-44fa-9f0c-462ec49c1ed1" />
SE GUARDAN LOS LIBROS INGRESADOS Y SE GUARDAN EN FIRE BASE
<img width="1417" height="564" alt="{665B8C47-1C2C-43B3-86F2-03DDC8BE258A}" src="https://github.com/user-attachments/assets/243d486e-13e8-4b46-a601-720443c1f202" />
<img width="499" height="460" alt="{A713D3C3-D640-4869-AFAF-2179C5ADD828}" src="https://github.com/user-attachments/assets/8a5237ec-1372-45dc-84b3-51db0c0174bd" />
MAS FUNCIONES
<img width="351" height="130" alt="{F5052FA9-2F3C-4306-94E2-519C931B6ADC}" src="https://github.com/user-attachments/assets/dfb69bab-9937-47ce-a5a0-cc56888550ef" />
Cambios Realizados en el Código

En la versión anterior del programa, toda la lógica estaba concentrada en una sola clase, lo que generaba confusión y hacía difícil mantener el código. Las listas de categorías y libros estaban separadas, repitiendo información innecesariamente y complicando la manipulación de datos. También faltaba una forma organizada de guardar y cargar la información, lo que hacía que los registros se perdieran al cerrar el programa.

En la nueva versión se realizaron varias mejoras importantes:

Se reestructuró el código aplicando un diseño más ordenado y modular.

Se creó la clase Biblioteca, que maneja de forma clara las categorías y libros, evitando repeticiones.

Se implementó la conexión con Firebase, permitiendo guardar y cargar los datos desde una base de datos en la nube.

Se agregó el uso de un archivo .env para manejar de manera segura las credenciales y la URL del proyecto.

Se mejoró la legibilidad, la validación de entradas y los mensajes de error para facilitar la experiencia del usuario.

<img width="1289" height="420" alt="{334EC44B-3B50-45F9-A82E-D361BF03540A}" src="https://github.com/user-attachments/assets/d45277f2-53e4-49b8-a33d-53f62a7ec781" />

