import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import os

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Agenda")
ventana.geometry("550x400")
ventana.attributes("-alpha", 0.9)
ventana.config(bg="Black")


modo_oscuro = True  # Estado inicial

colores = {
    "oscuro": {
        "bg": "black",
        "fg": "white",
        "boton_bg": "black",
        "boton_fg": "yellow",
        "tabla_bg": "white",
        "tabla_fg": "black",
        "encabezado_bg": "darkblue",
        "encabezado_fg": "white"
    },
    "claro": {
        "bg": "white",
        "fg": "black",
        "boton_bg": "lightgray",
        "boton_fg": "blue",
        "tabla_bg": "#f0f0f0",
        "tabla_fg": "black",
        "encabezado_bg": "skyblue",
        "encabezado_fg": "black"
    }
}

def cambiar_modo():
    global modo_oscuro
    modo_oscuro = not modo_oscuro
    tema = "oscuro" if modo_oscuro else "claro"
    c = colores[tema]

    ventana.config(bg=c["bg"])
    etiqueta.config(bg=c["bg"], fg=c["fg"])

    frame_eventos.config(bg=c["bg"])
    label_vacio.config(bg=c["bg"], fg="red")

    style.configure("Treeview", background=c["tabla_bg"], foreground=c["tabla_fg"], fieldbackground=c["tabla_bg"])
    style.configure("Treeview.Heading", background=c["encabezado_bg"], foreground=c["encabezado_fg"])

    for btn in [btn_agregar, btn_eliminar, btn_salir, btn_modo]:
        btn.config(bg=c["boton_bg"], fg=c["boton_fg"])

etiqueta = tk.Label(ventana, text="Bienvenido a su agenda", fg="white", bg="Black", font=("Arial", 12, "italic"))
etiqueta.pack()

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_modo = tk.Button(frame_botones, text="Modo Claro/Oscuro", command=cambiar_modo)
btn_modo.config(fg="yellow", bg="black", font=("Arial", 7, "bold"))
btn_modo.grid(row=0, column=0, padx=1)

# Crear estilo personalizado de la tabla
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview.Heading", background="darkblue", foreground="white", font=("Arial", 10, "bold"))
style.configure("Treeview", background="white", foreground="black", fieldbackground="white")

frame_eventos = tk.Frame(ventana)
frame_eventos.pack(pady=10)

tree = ttk.Treeview(frame_eventos, columns=("Fecha", "Hora", "Descripción"), show="headings", height=8)
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.column("Fecha", width=100)
tree.column("Hora", width=80)
tree.column("Descripción", width=300)
tree.pack()

# Etiqueta de vacío (se mostrará si no hay eventos)
label_vacio = tk.Label(frame_eventos, text="No tiene nada registrado", fg="red", font=("Arial", 10, "bold"))


# Función para cargar eventos desde archivo
def cargar_eventos():
    cargados = False
    if os.path.exists("eventos.csv"):
        with open("eventos.csv", "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) == 3:
                    tree.insert("", "end", values=partes)
                    cargados = True
    return cargados

# Mostrar mensaje si no hay eventos
if not cargar_eventos():
    label_vacio.pack()

# Función para añadir evento
def añadir_evento():
    ventana1 = tk.Toplevel()
    ventana1.title("Insertar Evento")
    ventana1.geometry("400x200")
    ventana1.config(bg="black")
    #ventana1.transient(ventana)
    ventana1.grab_set()
    #ventana.wait_window(ventana1)



    frame_entrada = tk.Frame(ventana1)
    frame_entrada.pack(pady=10)

    tk.Label(frame_entrada, text="Fecha:", fg="black").grid(row=0, column=0, padx=5, pady=5)
    entry_fecha = DateEntry(frame_entrada, date_pattern='dd/mm/yyyy')
    entry_fecha.config(background="#0F5950")
    entry_fecha.grid(row=0, column=1, padx=5)

    tk.Label(frame_entrada, text="Hora:", fg="black").grid(row=1, column=0, padx=5, pady=5)
    horas = [f"{h:02d}:{m:02d}" for h in range(0, 24) for m in (0, 15, 30, 45)]
    selector_hora = ttk.Combobox(frame_entrada, values=horas, state="readonly", width=10)
    selector_hora.grid(row=1, column=1, padx=5)

    tk.Label(frame_entrada, text="Descripción:", fg="black").grid(row=2, column=0, padx=5, pady=5)
    entry_desc = tk.Entry(frame_entrada, width=40)
    entry_desc.grid(row=2, column=1, padx=5)

    def guardar_evento():
        fecha = entry_fecha.get()
        hora = selector_hora.get()
        descripcion = entry_desc.get()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")
            return

        # Verificar si ya existe un evento con la misma fecha y hora
        for item in tree.get_children():
            valores = tree.item(item)["values"]
            if fecha == valores[0] and hora == valores[1]:
                messagebox.showerror("Conflicto de horario", f"Ya existe un evento registrado el {fecha} a las {hora}.")
                return

        if label_vacio.winfo_ismapped():
            label_vacio.pack_forget()

        tree.insert("", "end", values=(fecha, hora, descripcion))
        with open("eventos.csv", "a", encoding="utf-8") as f:
            f.write(f"{fecha},{hora},{descripcion}\n")
        ventana1.destroy()

    btn_guardar = tk.Button(ventana1, text="Guardar Evento", command=guardar_evento)
    btn_guardar.config(fg="yellow", bg="black", font=("Arial", 10, "bold"))
    btn_guardar.pack(pady=10)

# Función para eliminar evento
def eliminar_evento():
    seleccionado = tree.selection()
    if not seleccionado:
        messagebox.showinfo("Sin selección", "Selecciona un evento para eliminar.")
        return

    confirmar = messagebox.askyesno("Confirmar", "¿Deseas eliminar el evento seleccionado?")
    if confirmar:
        tree.delete(seleccionado)

        # Si no quedan eventos, mostrar el mensaje
        if not tree.get_children():
            label_vacio.pack()

# Función para salir
def salir():
    ventana.destroy()

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=añadir_evento)
btn_agregar.config(fg="yellow", bg="black", font=("Arial", 10, "bold"))
btn_agregar.grid(row=0, column=0, padx=1)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento)
btn_eliminar.config(fg="yellow", bg="black", font=("Arial", 10, "bold"))
btn_eliminar.grid(row=0, column=1, padx=1)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
btn_salir.config(fg="yellow", bg="black", font=("Arial", 10, "bold"))
btn_salir.grid(row=0, column=2, padx=1)

ventana.mainloop()

