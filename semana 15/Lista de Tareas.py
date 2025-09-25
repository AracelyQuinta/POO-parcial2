import tkinter as tk
from tkinter import ttk, messagebox

# Lista global para almacenar las tareas
tareas = []

# Función para actualizar la tabla de tareas en la ventana principal
def actualizar_tabla():
    # Elimina todas las filas actuales de la tabla
    for item in tabla.get_children():
        tabla.delete(item)

    # Si no hay tareas, muestra un mensaje motivador
    if not tareas:
        tabla.insert("", "end", values=("Escribe tu primera actividad a hacer", ""))
    else:
        # Si hay tareas, las muestra con su estado (completada o pendiente)
        for i, tarea in enumerate(tareas):
            estado = "✔️ Completada" if tarea["completada"] else "⏳ Pendiente"
            tabla.insert("", "end", iid=i, values=(tarea["descripcion"], estado))

# Función que abre una ventana emergente para añadir o eliminar tareas
def mas_acciones():
    ventana1 = tk.Toplevel()  # Crea una nueva ventana secundaria
    ventana1.title("Insertar Tarea")
    ventana1.grab_set()  # Bloquea la ventana principal hasta cerrar esta

    # Frame para la selección de acción
    frame_entrada = tk.Frame(ventana1)
    frame_entrada.pack(pady=10)

    # Etiqueta y combobox para elegir entre "Añadir" o "Eliminar"
    tk.Label(frame_entrada, text="Seleccione una acción:", fg="black").grid(row=0, column=0, padx=5, pady=5)
    combo_accion = ttk.Combobox(frame_entrada, values=["Añadir tarea", "Eliminar tarea"], state="readonly", width=20)
    combo_accion.grid(row=0, column=1, padx=5, pady=5)
    combo_accion.current(0)

    # Frame que se actualiza dinámicamente según la acción seleccionada
    frame_dinamico = tk.Frame(ventana1)
    frame_dinamico.pack(pady=10)

    # Función que muestra los campos correspondientes según la acción elegida
    def mostrar_opciones(event=None):
        # Limpia el contenido anterior del frame dinámico
        for widget in frame_dinamico.winfo_children():
            widget.destroy()

        accion = combo_accion.get()

        # Si se selecciona "Añadir tarea"
        if accion == "Añadir tarea":
            tk.Label(frame_dinamico, text="Descripción de la tarea:").pack()
            entry_tarea = tk.Entry(frame_dinamico, width=40)
            entry_tarea.pack(pady=5)

            # Función para agregar la tarea a la lista
            def agregar():
                desc = entry_tarea.get().strip()
                if desc:
                    tareas.append({"descripcion": desc, "completada": False})
                    actualizar_tabla()
                    ventana1.destroy()
                else:
                    messagebox.showwarning("Advertencia", "La descripción no puede estar vacía.")

            tk.Button(frame_dinamico, text="Agregar", command=agregar).pack(pady=5)

        # Si se selecciona "Eliminar tarea"
        elif accion == "Eliminar tarea":
            if not tareas:
                tk.Label(frame_dinamico, text="No hay tareas para eliminar.").pack()
                return

            tk.Label(frame_dinamico, text="Seleccione tarea a eliminar:").pack()
            lista_tareas = ttk.Combobox(frame_dinamico, values=[t["descripcion"] for t in tareas], state="readonly", width=40)
            lista_tareas.pack(pady=5)

            # Función para eliminar la tarea seleccionada
            def eliminar():
                seleccion = lista_tareas.get()
                if seleccion:
                    tareas[:] = [t for t in tareas if t["descripcion"] != seleccion]
                    actualizar_tabla()
                    ventana1.destroy()
                else:
                    messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

            botones_frame = tk.Frame(frame_dinamico)
            botones_frame.pack(pady=5)

            tk.Button(botones_frame, text="Eliminar", command=eliminar).pack(side="left", padx=10)
            tk.Button(botones_frame, text="Cancelar", command=ventana1.destroy).pack(side="left", padx=10)

    # Detecta cuando se cambia la opción del combobox
    combo_accion.bind("<<ComboboxSelected>>", mostrar_opciones)
    mostrar_opciones()  # Muestra la opción inicial

# Función que se ejecuta al hacer doble clic en una tarea para marcarla como completada
def marcar_completada(event):
    seleccion = tabla.selection()
    if seleccion:
        idx = seleccion[0]
        if idx.isdigit():  # Verifica que el índice sea válido
            tareas[int(idx)]["completada"] = not tareas[int(idx)]["completada"]
            actualizar_tabla()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Lista de tareas")
ventana.geometry("600x400")
ventana.resizable(False, False)

# Título principal
tk.Label(ventana, text="Lista de tareas", font=("Arial", 14, "bold")).pack(pady=10)

# Tabla para mostrar las tareas y su estado
tabla = ttk.Treeview(ventana, columns=("Tarea", "Estado"), show="headings", selectmode="browse")
tabla.heading("Tarea", text="Tarea")
tabla.heading("Estado", text="Estado")
tabla.pack(pady=10, fill="both", expand=True)
tabla.bind("<Double-1>", marcar_completada)  # Doble clic para marcar como completada

# Botón para abrir la ventana de acciones
boton = tk.Button(ventana, text="Más acciones", command=mas_acciones)
boton.config(fg="Purple", font=("Arial", 12, "bold"))
boton.pack(pady=10)

# Inicializa la tabla al arrancar
actualizar_tabla()

# Ejecuta la aplicación
ventana.mainloop()