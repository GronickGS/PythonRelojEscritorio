from tkinter import Label, Tk, Button
import time

ventana = Tk()
ventana.config(bg='gray')
ventana.geometry('600x250')
ventana.wm_attributes("-transparentcolor", 'gray')

ventana.overrideredirect(1)


def salir(*arg):
    ventana.destroy()
    ventana.quit()


def obtener_tiempo():
    hora = time.strftime('%H:%M:%S')
    GS = "GRONICK"
    fecha = time.strftime('%A' ' ' '%d' ' ' '%B' ' ' '%Y')

    textoHora['text'] = hora
    textoGS['text'] = GS
    textFecha['text'] = fecha
    textoHora.after(1000, obtener_tiempo)

def start(event):
    global x, y
    x = event.x
    y = event.y

def stop(event):
    global x, y
    x = None
    y = None

def mover(event):
    global x, y
    deltax = event.x - x
    deltay = event.y - y
    ventana.geometry("+%s+%s" % (ventana.winfo_x() + deltax, ventana.winfo_y() + deltay))
    ventana.update()

ventana.bind("<ButtonPress-1>", start)
ventana.bind("<ButtonRelease-1>", stop)
ventana.bind("<B1-Motion>", mover)
ventana.bind("<KeyPress-Escape>", salir)

textoHora = Label(ventana, fg="white", bg="gray", font=('Times New Roman', 70), width=10)
textoHora.grid(column=0, row=0, ipadx=1, ipady=1)

textFecha = Label(ventana, fg="white", bg="gray", font=('Times New Roman', 20))
textFecha.grid(column=0, row=1)

textoGS = Label(ventana, fg="white", bg="gray", font=('Courier', 20, 'bold'))
textoGS.grid(column=0, row=2)

obtener_tiempo()

botonCerrar = Button(ventana, text="Cerrar", command=salir, fg='white', bg='gray', relief='flat')
botonCerrar.grid(column=0, row=3)

ventana.mainloop()
