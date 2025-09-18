import tkinter as tk


ventana =tk.Tk()
ventana.title("Ejemplo label")

# TRAE UNA ETIQUETA EN  UNA VENTANA ES MEJOR EN FRAME DENTRO DE UNA VENTANA PARA TEXTO SOLO TEXT=" PARA QUE SE VEA ES ETIQUETA. PACK
# Y PARA QUE SE VEA SIEMPRE EL VENTANA.MAINLOOP()
etiqueta =tk.Label(ventana, text="hola soy un label")
#etiqueta.config(texto= "Hola")
etiqueta.config(fg="blue", bg="yellow", font=("Arial",12,"bold"))# italic para cursiva
etiqueta.pack()

ventana.mainloop()
