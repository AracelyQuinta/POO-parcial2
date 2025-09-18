import time
import tkinter as tk

ventana=tk.Tk()
ventana.title("Ejemplo Label")
ventana.geometry("200x100")

etiqueta = tk.Label(ventana, text="Lo de abajo es un entry")
etiqueta.pack()

entrada=tk.Entry(ventana)
entrada.config(fg="white",bg= "black",font=("Arial", 12,"bold"))
entrada.pack()


# para tener un texto por defecto se debe codificar asi
entrada.insert(0, "Texto por defecto")

#texto = entrada.get()
#print(texto)

# al cambiar el texto cambia el label
def aplicar_texto():
    texto=entrada.get()
    etiqueta.config(text=texto)

boton_aplicar =tk.Button(ventana, text="Aplicar", command=aplicar_texto)
boton_aplicar.pack()


ventana.mainloop()