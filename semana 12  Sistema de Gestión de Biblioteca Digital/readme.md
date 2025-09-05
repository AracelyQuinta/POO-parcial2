# Sistema de Gestión de Biblioteca Digita
El sistema se compone de varias clases y módulos que trabajan en conjunto para ofrecer funcionalidades como:
- Registro de usuarios: permite crear perfiles únicos con nombre e ID.
- Gestión de libros: cada libro tiene atributos como título, autor, categoría e ISBN.
- Préstamo y devolución: los usuarios pueden solicitar libros disponibles y devolverlos cuando terminen.
- Búsqueda avanzada: se puede localizar libros por título, autor, categoría o ISBN.
- Persistencia de datos: toda la información se guarda automáticamente en archivos .txt, lo que permite conservar el historial sin necesidad de bases de datos externas.
- Menú interactivo: guía al usuario paso a paso con opciones claras y validaciones lógicas.

## clases necesarias para que el sistema funcione. Cada clase tiene una responsabilidad específica:
- Biblioteca: gestiona usuarios, libros, préstamos y devoluciones.
- Reporte: genera informes y estadísticas.
- GuardarT: maneja la persistencia de datos en archivos .txt.
- Usuario y Libro: representan los objetos principales del sistema.

El sistema entra en un bucle while True donde muestra el menú y espera una opción del usuario. Cada opción ejecuta una función específica:
- Opción 1: Agrega un nuevo libro al catálogo.
- Opción 2: Permite al usuario actual solicitar un préstamo.
- Opción 3: Permite devolver un libro prestado.
- Opción 4: Muestra todos los usuarios registrados.
- Opción 5: Muestra el catálogo completo de libros.
- Opción 6: Permite buscar libros por distintos criterios.
- Opción 7: Lista los libros prestados por cada usuario.
- Opción 8: Muestra el estado general de todos los libros.
- Opción 9: Abre el menú de reportes.
- Opción 10: Da de baja al usuario actual tras confirmación.
- Opción 0: Guarda los datos y cierra el sistema.
Cada acción que modifica datos llama a persistencia.guardar_todo_txt() para asegurar que los cambios se guarden correctamente.
# Resultados de las opciones seleccionadas:


### Resultado obtenido al igresar al sistema
<img width="540" height="157" alt="image" src="https://github.com/user-attachments/assets/67954904-2477-490e-9b33-ff4ae67406fb" />


### Muestra el menu interactivo
<img width="398" height="324" alt="image" src="https://github.com/user-attachments/assets/69d9b569-7bf9-49a4-b9ee-d83df677301d" />

Opcion 1:
### Resultado obtenido al Agregar nuevo libro
<img width="309" height="287" alt="image" src="https://github.com/user-attachments/assets/2e5b5af7-ee95-46ae-bd84-74f5297040e5" />

Opcion 2:
### Resultado obtenido al Prestar libro
<img width="428" height="341" alt="image" src="https://github.com/user-attachments/assets/5e38c482-ca72-48f8-b3af-524379539971" />

Opcion 3:
### Resultado obtenido al Devolver libro
<img width="822" height="434" alt="image" src="https://github.com/user-attachments/assets/2ef1458b-6f8c-41ca-8262-14ed7fb1581c" />

Opcion 4:
### Resultado obtenido al Mostrar usuarios registrados
<img width="357" height="504" alt="image" src="https://github.com/user-attachments/assets/2bc489f3-c443-49b8-a0d8-c873e088ec28" />

Opcion 5:
### Resultado obtenido al Mostrar catálogo de libros
<img width="901" height="224" alt="image" src="https://github.com/user-attachments/assets/7c5f163e-b310-4777-b3a5-02cf581fcbe7" />

Opcion 6:
### Resultado obtenido al  Buscar libros
<img width="905" height="203" alt="image" src="https://github.com/user-attachments/assets/41d60b5f-7d98-47e6-a175-a5592c75741f" />

Opcion 7:
### Resultado obtenido al Listar libros prestados por usuario
<img width="789" height="210" alt="image" src="https://github.com/user-attachments/assets/d2822aaa-4f18-4ecc-9b37-b546fde48df9" />

Opcion 8:
### Resultado obtenido al Mostrar estado general de libros
<img width="816" height="325" alt="image" src="https://github.com/user-attachments/assets/f7990acf-1550-4d00-b136-39f7de59334e" />

Opcion 9:
### Resultado obtenido al Generar reporte de los libros
<img width="302" height="116" alt="image" src="https://github.com/user-attachments/assets/0c4e9c43-0a69-4e71-ac74-b0dac06380ad" />

Opcion 10:
### Resultado obtenido al  Dar de baja usuario
<img width="609" height="147" alt="image" src="https://github.com/user-attachments/assets/27fe81df-3752-47fc-a76f-067bf1a04da6" />

Este archivo permite que el sistema funcione como una aplicación interactiva, donde el usuario puede navegar por las opciones, realizar operaciones y ver resultados en tiempo real
