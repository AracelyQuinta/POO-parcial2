
import tkinter as tk
from tkinter import ttk, messagebox

# Función para agregar producto a la tabla
def agregar_producto():
    desconocido = entry_desc.get()
    try:
        cantidad = int(entry_cant.get())
        precio = float(entry_precio.get())
    except ValueError:
        messagebox.showerror("Error", "Cantidad y precio deben ser numéricos.")
        return

    if desconocido.strip() == "":
        messagebox.showwarning("Campo vacío", "La descripción no puede estar vacía.")
        return

    total = cantidad * precio
    tabla.insert("", "end", values=(desconocido, cantidad, f"${precio:.2f}", f"${total:.2f}"))
    entry_desc.delete(0, tk.END)
    entry_cant.delete(0, tk.END)
    entry_precio.delete(0, tk.END)

# Función para limpiar todo
def limpiar():
    entry_cliente.delete(0, tk.END)
    entry_cedula.delete(0, tk.END)
    entry_desc.delete(0, tk.END)
    entry_cant.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    tabla.delete(*tabla.get_children())
    label_total.config(text="Total: $0.00")

# Función para calcular el total
def calcular_total():
    total = 0
    for item in tabla.get_children():
        valores = tabla.item(item, "values")
        total += float(valores[3].replace("$", ""))
    label_total.config(text=f"Total: ${total:.2f}")

# Ventana principal
ventana = tk.Tk()
ventana.title("Factura de Venta")
ventana.geometry("600x500")
#ventana.resizable(False, False)
ventana.iconbitmap("icono.ico")

# Datos del cliente
frame_cliente = tk.LabelFrame(ventana, text="Datos del Cliente")
frame_cliente.pack(fill="x", padx=10, pady=5)

tk.Label(frame_cliente, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
entry_cliente = tk.Entry(frame_cliente, width=30)
entry_cliente.grid(row=0, column=1)

tk.Label(frame_cliente, text="Cédula:").grid(row=0, column=2, padx=5)
entry_cedula = tk.Entry(frame_cliente, width=20)
entry_cedula.grid(row=0, column=3)

# Datos del producto
frame_producto = tk.LabelFrame(ventana, text="Agregar Producto")
frame_producto.pack(fill="x", padx=10, pady=5)

tk.Label(frame_producto, text="Descripción:").grid(row=0, column=0, padx=5, pady=5)
entry_desc = tk.Entry(frame_producto, width=25)
entry_desc.grid(row=0, column=1)

tk.Label(frame_producto, text="Cantidad:").grid(row=0, column=2)
entry_cant = tk.Entry(frame_producto, width=10)
entry_cant.grid(row=0, column=3)

tk.Label(frame_producto, text="Precio Unitario:").grid(row=0, column=4)
entry_precio = tk.Entry(frame_producto, width=10)
entry_precio.grid(row=0, column=5)

tk.Button(frame_producto, text="Agregar producto", command=agregar_producto, bg="#4CAF50", fg="white").grid(row=0, column=6, padx=10)

# Tabla de productos
frame_tabla = tk.Frame(ventana)
frame_tabla.pack(padx=10, pady=10)

tabla = ttk.Treeview(frame_tabla, columns=("desc", "cant", "precio", "total"), show="headings", height=8)
tabla.heading("desc", text="Descripción")
tabla.heading("cant", text="Cantidad")
tabla.heading("precio", text="Precio Unitario")
tabla.heading("total", text="Total")

tabla.column("desc", width=200)
tabla.column("cant", width=80, anchor="center")
tabla.column("precio", width=100, anchor="center")
tabla.column("total", width=100, anchor="center")

tabla.pack(side="left")

scroll = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scroll.set)
scroll.pack(side="right", fill="y")

# Total y botones
frame_total = tk.Frame(ventana)
frame_total.pack(fill="x", padx=10, pady=10)

label_total = tk.Label(frame_total, text="Total: $0.00", font=("Arial", 12, "bold"))
label_total.pack(side="left")

tk.Button(frame_total, text="Generar Total", command=calcular_total, bg="#2196F3", fg="white").pack(side="right", padx=5)
tk.Button(frame_total, text="Limpiar", command=limpiar, bg="#f44336", fg="white").pack(side="right", padx=5)

ventana.mainloop()