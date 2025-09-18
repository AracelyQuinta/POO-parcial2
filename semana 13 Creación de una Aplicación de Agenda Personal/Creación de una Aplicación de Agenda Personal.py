import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_desc.get()

    if not fecha or not hora or not descripcion:
        messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")
        return

    tree.insert("", "end", values=(fecha, hora, descripcion))
    entry_hora.delete(0, tk.END)
    entry_desc.delete(0, tk.END)

# Función para eliminar evento
def eliminar_evento():
    seleccionado = tree.selection()
    if not seleccionado:
        messagebox.showinfo("Sin selección", "Selecciona un evento para eliminar.")
        return

    confirmar = messagebox.askyesno("Confirmar", "¿Deseas eliminar el evento seleccionado?")
    if confirmar:
        tree.delete(seleccionado)

# Función para salir
def salir():
    ventana.destroy()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("600x400")
ventana.resizable(False, False)

# ───── Frame: Lista de eventos ─────
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

# ───── Frame: Entrada de datos ─────
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
entry_fecha = DateEntry(frame_entrada, date_pattern='dd/mm/yyyy')
entry_fecha.grid(row=0, column=1, padx=5)

tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=5)

tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
entry_desc = tk.Entry(frame_entrada, width=40)
entry_desc.grid(row=2, column=1, padx=5)

# ───── Frame: Botones ─────
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.config(fg="yellow", bg="black", font=("Arial", 10,"bold"))
btn_agregar.grid(row=0, column=0, padx=10)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.config(fg="yellow", bg="black", font=("Arial", 10,"bold"))
btn_eliminar.grid(row=0, column=1, padx=10)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
btn_salir.config(fg="yellow", bg="black", font=("Arial", 10,"bold"))
btn_salir.grid(row=0, column=2, padx=10)

ventana.mainloop()