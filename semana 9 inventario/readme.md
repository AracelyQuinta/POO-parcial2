#  Sistema de Gestión de Inventarios
El sistema permite al usuario gestionar productos mediante un menú interactivo, con las siguientes funcionalidades:
## 1. Añadir productos
- Solicita al usuario el ID, nombre, cantidad y precio del producto.
- Verifica que el ID no esté duplicado en la lista en memoria.
- Si es válido, crea una instancia de Producto y la guarda en memoria.
- Luego, guarda todos los productos en un archivo Excel (.xlsx), añadiéndolos al final sin borrar los anteriores.

<img width="641" height="653" alt="image" src="https://github.com/user-attachments/assets/d20a6ba4-04c6-4953-a1e0-5b85ec1d9c2e" />
<img width="716" height="307" alt="image" src="https://github.com/user-attachments/assets/42265843-f43b-4112-b04c-6a7a27df6959" />
<img width="345" height="498" alt="image" src="https://github.com/user-attachments/assets/c277e749-c857-424c-8eff-0edb807b0c35" />
  
## 2. Eliminar productos
- Solicita el ID del producto a eliminar.
- Busca ese ID en el archivo Excel y elimina la fila correspondiente si existe.
- Guarda los cambios y abre el archivo para mostrar el resultado.

<img width="490" height="319" alt="image" src="https://github.com/user-attachments/assets/5ae61747-a6db-4139-8dab-831fd4b16ca2" />
<img width="442" height="362" alt="image" src="https://github.com/user-attachments/assets/9ed86cbc-c316-4a5c-93ed-2d2444f7ecb2" />

## 3. Actualizar productos
- Solicita el ID del producto a actualizar.
- Muestra los datos actuales del producto en Excel.
- Permite al usuario elegir qué campos desea modificar: nombre, cantidad, precio o todos.
- Valida cada entrada antes de actualizar y guarda los cambios en el archivo.

 <img width="592" height="613" alt="image" src="https://github.com/user-attachments/assets/7e8d2ad6-0383-47ef-a2a7-14ac4ee9b12c" />
 <img width="427" height="260" alt="image" src="https://github.com/user-attachments/assets/ca9f74af-0fab-4f6d-b200-47b189602dd2" />

## 4. Buscar productos por nombre
- Solicita un texto de búsqueda.
- Recorre el archivo Excel y muestra todos los productos cuyo nombre contenga ese texto (sin importar mayúsculas/minúsculas).

<img width="568" height="302" alt="image" src="https://github.com/user-attachments/assets/461a35fc-c201-4792-ab87-83e9e4bf61b5" />

## 5. Mostrar todos los productos
- Lee el archivo Excel y muestra todos los productos registrados en una tabla ordenada con columnas: ID, Nombre, Cantidad, Precio.

<img width="580" height="575" alt="image" src="https://github.com/user-attachments/assets/9a3bc728-67e2-4ee4-8bd4-7cd5076f5887" />

## 6. Salir del sistema
- Finaliza el programa de forma segura.

  <img width="389" height="311" alt="image" src="https://github.com/user-attachments/assets/102fd69d-5f4f-4b8f-9ebe-86fc0dcccfa7" />

