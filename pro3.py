"""
Created on Tue Nov  9 13:08:48 2021

@author: Faryd Torres S
"""

import tkinter.ttk
from tkinter import *
from tkinter import messagebox


class Ventana(Tk):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.geometry("650x550")

        self.title("Bienvenido")

        self.resizable(0, 0)

        self.rowconfigure(0, weight=1)

        self.columnconfigure(0, weight=1)

        self.paginas = dict()

        for f in (Pagina_1, V2):

            frame = f(self, self)

            self.paginas[f] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.cambio_pagina(Pagina_1)

    def cambio_pagina(self, pagina_llamada):

        frame = self.paginas[pagina_llamada]

        frame.tkraise()


class Pagina_1(Frame):

    def __init__(self, contenedor, controlador, *args, **kwargs):

        super().__init__(contenedor, *args, **kwargs)

        menu_principal_1 = Frame(self)

        menu_principal_1.pack(expand=1)

        username_label = Label(menu_principal_1, text=" Bienvenido ")

        username_label.pack(pady=10)

        submit_btn = Button(menu_principal_1, text="Siguiente", width="30",
                            height="2", bg="#00CD63", command=lambda: controlador.cambio_pagina(V2))

        submit_btn.pack()


class V2(Frame):

    def __init__(self, contenedor, controlador, *args, **kwargs):

        super().__init__(contenedor, *args, **kwargs)

        self.config(bg="#273746")

        username = StringVar()
        password = StringVar()
        fullname = StringVar()
        age = StringVar()

        menu_principal_2 = Frame(self, bg="#273746")
        menu_principal_2.pack(expand=1)

        username_label = Label(menu_principal_2, text="USUARIO", bg="#D5DBDB")
        username_label.grid(row=1, column=1)

        password_label = Label(
            menu_principal_2, text="CONTRASEÑA", bg="#D5DBDB")
        password_label.grid(row=2, column=1)

        username_entry = Entry(
            menu_principal_2, textvariable=username, width="40")
        username_entry.grid(row=1, column=2)

        password_entry = Entry(
            menu_principal_2, textvariable=password, width="40", show="*")
        password_entry.grid(row=2, column=2)

        c1 = Checkbutton(menu_principal_2, text="RECORDAR MIS DATOS",
                         onvalue=1, offvalue=0, bg="#273746", font='Helvetica 7 bold')
        c1.grid(row=4, column=2)

        submit_btn = Button(menu_principal_2, text="Ingresar",
                            width="30", height="2", bg="#00CD63")
        submit_btn.grid(row=5, columnspan=3)


if __name__ == "__main__":
    app = Ventana()
    app.mainloop()
