import tkinter
from tkinter import messagebox

name = ""
user = ""
password = ""


def openAppWindow():
    def playMessage():
        messagebox.showinfo(
            message="El PC recomendado para jugar es: Tarjeta grafica RTX 3080 y un procesador Ryzen 9 5950x (enfocado en gaming de alto rendimiento)", title="Recomendacion")

    def workMessage():
        messagebox.showinfo(
            message="El PC recomendado para trabajar es: Tarjeta grafica GT 710 y un procesador Ryzen 3 3100 (enfocado solo para trabajo basico)", title="Recomendacion")

    def bothMessage():
        messagebox.showinfo(
            message="El PC recomendado para jugar y trabajar es: Tarjeta grafica RTX 3060 y un procesador Ryzen 5 3600 (enfocado en ambas cosas)", title="Recomendacion")

    windowApp = tkinter.Tk()
    windowApp.geometry("800x600")
    windowApp.title("Recomendacion de PC")
    labelName = tkinter.Label(
        windowApp, text="Bievenido, "+name, font=("OpenSans", 30))
    labelName.grid(row=0, column=0)
    labelName.place(x=400, y=50, anchor="center")
    labelTitle = tkinter.Label(
        windowApp, text="¿Que uso le dara al computador?", font=("OpenSans", 30))
    labelTitle.grid(row=0, column=0)
    labelTitle.place(x=400, y=150, anchor="center")
    buttonPlay = tkinter.Button(
        windowApp, text="Jugar", command=playMessage, font=("OpenSans", 15))
    buttonPlay.grid(row=4, column=0)
    buttonPlay.place(x=300, y=250, anchor="center")
    buttonWork = tkinter.Button(
        windowApp, text="Trabajar", command=workMessage, font=("OpenSans", 15))
    buttonWork.grid(row=4, column=0)
    buttonWork.place(x=400, y=250, anchor="center")
    buttonBoth = tkinter.Button(
        windowApp, text="Ambos", command=bothMessage, font=("OpenSans", 15))
    buttonBoth.grid(row=4, column=0)
    buttonBoth.place(x=500, y=250, anchor="center")


def openLoginWindow():
    def verifyCredentials():
        if(inputUser.get() != "" and inputPassword.get() != ""):
            global user, password, name
            if(inputUser.get() == user and inputPassword.get() == password):
                messagebox.showinfo(
                    message="Credenciales correctas", title="Inicio de sesion correcto")
                windowLogin.destroy()
                openAppWindow()
            else:
                messagebox.showerror(
                    message="Credenciales incorrectas", title="Error de inicio de sesion")
        else:
            messagebox.showerror(
                message="No has completado todos los datos", title="Error de datos")
    windowLogin = tkinter.Tk()
    windowLogin.geometry("800x600")
    windowLogin.title("Inicio de sesion")
    labelTitle = tkinter.Label(
        windowLogin, text="Inicio de sesion", font=("OpenSans", 30))
    labelTitle.grid(row=0, column=0)
    labelTitle.place(x=400, y=100, anchor="center")
    labelUser = tkinter.Label(
        windowLogin, text="Usuario:", font=("OpenSans", 15))
    labelUser.grid(row=2, column=0)
    labelUser.place(x=200, y=250, anchor="center")
    inputUser = tkinter.Entry(windowLogin, font=("OpenSans", 12))
    inputUser.grid(row=2, column=1)
    inputUser.place(x=400, y=250, anchor="center", width=200, height=30)
    labelPassword = tkinter.Label(
        windowLogin, text="Contraseña:", font=("OpenSans", 15))
    labelPassword.grid(row=3, column=0)
    labelPassword.place(x=200, y=300, anchor="center")
    inputPassword = tkinter.Entry(windowLogin, font=("OpenSans", 12))
    inputPassword.grid(row=3, column=1)
    inputPassword.place(x=400, y=300, anchor="center", width=200, height=30)
    buttonRegister = tkinter.Button(
        windowLogin, text="Iniciar sesion", command=verifyCredentials, font=("OpenSans", 15))
    buttonRegister.grid(row=4, column=0)
    buttonRegister.place(x=400, y=400, anchor="center")
    windowLogin.mainloop()


def registerWindow():
    def registerDataUser():
        global name, user, password
        if(inputName.get() != "" and inputUser.get() != "" and inputPassword.get() != ""):
            name = inputName.get()
            user = inputUser.get()
            password = inputPassword.get()
            messagebox.showinfo(
                message="Registro de usuario correcto", title="Registro correcto")
            windowRegister.destroy()
            openLoginWindow()
        else:
            messagebox.showerror(
                message="No has completado todos los datos", title="Error de datos")
    windowRegister = tkinter.Tk()
    windowRegister.geometry("800x600")
    windowRegister.title("Registro de usuarios")
    labelTitle = tkinter.Label(
        windowRegister, text="Registro de usuarios", font=("OpenSans", 30))
    labelTitle.grid(row=0, column=0)
    labelTitle.place(x=400, y=100, anchor="center")
    labelName = tkinter.Label(
        windowRegister, text="Nombre:", font=("OpenSans", 15))
    labelName.grid(row=1, column=0)
    labelName.place(x=200, y=200, anchor="center")
    inputName = tkinter.Entry(windowRegister, font=("OpenSans", 12))
    inputName.grid(row=1, column=1)
    inputName.place(x=400, y=200, anchor="center", width=200, height=30)
    labelUser = tkinter.Label(
        windowRegister, text="Usuario:", font=("OpenSans", 15))
    labelUser.grid(row=2, column=0)
    labelUser.place(x=200, y=250, anchor="center")
    inputUser = tkinter.Entry(windowRegister, font=("OpenSans", 12))
    inputUser.grid(row=2, column=1)
    inputUser.place(x=400, y=250, anchor="center", width=200, height=30)
    labelPassword = tkinter.Label(
        windowRegister, text="Contraseña:", font=("OpenSans", 15))
    labelPassword.grid(row=3, column=0)
    labelPassword.place(x=200, y=300, anchor="center")
    inputPassword = tkinter.Entry(windowRegister, font=("OpenSans", 12))
    inputPassword.grid(row=3, column=1)
    inputPassword.place(x=400, y=300, anchor="center", width=200, height=30)
    buttonRegister = tkinter.Button(
        windowRegister, text="Registrarse", command=registerDataUser, font=("OpenSans", 15))
    buttonRegister.grid(row=4, column=0)
    buttonRegister.place(x=400, y=400, anchor="center")
    windowRegister.mainloop()


registerWindow()
