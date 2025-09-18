import time
import tkinter as tk

ventana=tk.Tk()
ventana.title("Ejemplo Label")

boton= tk.Button(ventana, text="Presioname")
boton.config(fg= "Purple",bg= "yellow",font=("Arial", 12,"bold"))
boton.pack()

etiqueta = tk.Label(ventana, text="Etiqueta label")
etiqueta.pack()

def cambiar_texto():
    etiqueta.config(text="¡Boton presionado!")
"""
# Reloj
etiqueta = tk.Label(ventana, text="Hola soy Label")
etiqueta.config(fg="blue", bg="white",font=("Arial",20,"italic"))
etiqueta.pack()

def actualizar_hora():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    ventana.after(1000, actualizar_hora)


actualizar_hora()


#funcion del boton
def boton_presioname():
    print("Boton presionado!")


boton.configure(command=boton_presioname)
"""

boton.configure(command=cambiar_texto)
ventana.mainloop()
