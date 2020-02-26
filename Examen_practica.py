import tkinter as tk
from tkinter import ttk, messagebox, Menu


ventana = tk.Tk()
EntryArr = []
Label = ["¿Que es la analisis psicologico?", "¿Como se lee la mente?", "¿Cuantas persepciones psicologicas existen?", "¿Padre de la Psicologia moderna?", "Parte del cuerpo donde esta la psyco"]
Arr3 = tk.IntVar()
opciones1 = ["1", "2","5"]
opciones2 = ["John Lenon", "Leon Borrego", "Jefry", "mxrio"]
opciones3 = ["Cabeza", "mente", "Pecho", "corazon", "Manos"]
respuesta = dict.fromkeys(opciones3, None)

def grid(Component, col, row1, padx1, pady1):
    Component.grid(column=col, row=row1, padx=padx1, pady=pady1)

def click():
    i = 0
    cal = 0
    info = ""
    for x in EntryArr:
        if not x.get():
            messagebox.showinfo("Error","Campos no llenos")
            return
        else: 
            info += (f"{Label[i]}\t{x.get()}"+ "\n")
            cal = 40
            i+= 1

    if(Arr3.get() == 1):
        cal+= 20
    if (Arr4.get() == 2):
        cal+= 20
    messagebox.showinfo("resultados","Tu calificaion es"+ cal )



Arr3 = tk.IntVar()
Arr4 = tk.IntVar()



def edicion1():
   
    indice = 0
    for i in range(0,2):
        EntryArr.append(tk.StringVar())
        grid(
            ttk.Entry(ventana, textvariable=EntryArr[indice]), 1, indice, 10, 10)
        grid(ttk.Label(ventana, text=Label[i]), 0, indice, 10, 10)
        indice += 1
    grid(ttk.Label(ventana, text=Label[2]), 0, indice, 10, 10)
    icol = 1
    Arr3 = tk.IntVar()
    for i in range(0,3):
        grid(ttk.Radiobutton(ventana, text = opciones1[i], variable=Arr3, value = i), icol, 2, 5, 5)
        icol +=1
   
    icol = 1
    grid(ttk.Label(ventana, text=Label[3]), 0, 3, 10, 10)
    for i in range(0,4):
        grid(ttk.Radiobutton(ventana, text = opciones2[i], variable=Arr4, value = i), icol, 3, 5, 5)
        icol +=1
        # Botton
    grid(ttk.Label(ventana, text=Label[4]), 0, 4, 10, 10)
    icol = 0
    for key in respuesta:
        respuesta[key] = tk.IntVar()
        ttk.Checkbutton(ventana, text = key, variable = respuesta[key]).grid(row = 5, column = icol)
        icol = icol + 1  


    Botton = tk.Button(ventana, text="Aceptar", command = click)
    grid(Botton, 2, 10, 10, 10)




def main():
    edicion1()
    ventana.mainloop()


main()
