import tkinter as tk
from tkinter import ttk, messagebox

tareas = []

def actualizar_tabla():
    for item in tabla.get_children():
        tabla.delete(item)

    if not tareas:
        tabla.insert("", "end", values=("Escribe tu primera actividad a hacer", ""))
    else:
        for i, tarea in enumerate(tareas):
            estado = "✔️ Completada" if tarea["completada"] else "⏳ Pendiente"
            tabla.insert("", "end", iid=i, values=(tarea["descripcion"], estado))

def mas_acciones():
    ventana1 = tk.Toplevel()
    ventana1.title("Insertar Tarea")
    ventana1.grab_set()

    frame_entrada = tk.Frame(ventana1)
    frame_entrada.pack(pady=10)

    tk.Label(frame_entrada, text="Seleccione una acción:", fg="black").grid(row=0, column=0, padx=5, pady=5)
    combo_accion = ttk.Combobox(frame_entrada, values=["Añadir tarea", "Eliminar tarea"], state="readonly", width=20)
    combo_accion.grid(row=0, column=1, padx=5, pady=5)
    combo_accion.current(0)

    frame_dinamico = tk.Frame(ventana1)
    frame_dinamico.pack(pady=10)

    def mostrar_opciones(event=None):
        for widget in frame_dinamico.winfo_children():
            widget.destroy()

        accion = combo_accion.get()

        if accion == "Añadir tarea":
            tk.Label(frame_dinamico, text="Descripción de la tarea:").pack()
            entry_tarea = tk.Entry(frame_dinamico, width=40)
            entry_tarea.pack(pady=5)

            def agregar():
                desc = entry_tarea.get().strip()
                if desc:
                    tareas.append({"descripcion": desc, "completada": False})
                    actualizar_tabla()
                    ventana1.destroy()
                else:
                    messagebox.showwarning("Advertencia", "La descripción no puede estar vacía.")

            tk.Button(frame_dinamico, text="Agregar", command=agregar).pack(pady=5)

        elif accion == "Eliminar tarea":
            if not tareas:
                tk.Label(frame_dinamico, text="No hay tareas para eliminar.").pack()
                return

            tk.Label(frame_dinamico, text="Seleccione tarea a eliminar:").pack()
            lista_tareas = ttk.Combobox(frame_dinamico, values=[t["descripcion"] for t in tareas], state="readonly", width=40)
            lista_tareas.pack(pady=5)

            def eliminar():
                seleccion = lista_tareas.get()
                if seleccion:
                    tareas[:] = [t for t in tareas if t["descripcion"] != seleccion]
                    actualizar_tabla()
                    ventana1.destroy()
                else:
                    messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

            tk.Button(frame_dinamico, text="Eliminar", command=eliminar).pack(pady=5)

    combo_accion.bind("<<ComboboxSelected>>", mostrar_opciones)
    mostrar_opciones()

def marcar_completada(event):
    seleccion = tabla.selection()
    if seleccion:
        idx = seleccion[0]
        if idx.isdigit():
            tareas[int(idx)]["completada"] = not tareas[int(idx)]["completada"]
            actualizar_tabla()

ventana = tk.Tk()
ventana.title("Lista de tareas")
ventana.geometry("600x400")
ventana.resizable(False, False)

tk.Label(ventana, text="Lista de tareas", font=("Arial", 14, "bold")).pack(pady=10)

tabla = ttk.Treeview(ventana, columns=("Tarea", "Estado"), show="headings", selectmode="browse")
tabla.heading("Tarea", text="Tarea")
tabla.heading("Estado", text="Estado")
tabla.pack(pady=10, fill="both", expand=True)
tabla.bind("<Double-1>", marcar_completada)

boton = tk.Button(ventana, text="Más acciones", command=mas_acciones)
boton.config(fg="Purple", font=("Arial", 12, "bold"))
boton.pack(pady=10)

actualizar_tabla()
ventana.mainloop()


