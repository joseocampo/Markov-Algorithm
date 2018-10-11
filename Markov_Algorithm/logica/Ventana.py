from tkinter import *
# THE NEXT IMPORT LET US TO USE THE FLOATING WINDOWS.
from tkinter import messagebox
from tkinter import filedialog
from functools import partial
from sys import getsizeof
from io import open
from os import path


class Ventana():

# este es un comentario para hacer commit
    def __init__(self):
        self.initializeComponents()
        self.__selectedNumber = StringVar()
        self.addWidgetsLeftFrame()
        self.readDefaultAlgorimth()
        self.createMenu()
        self.__optionCloseApp = False
        self.__file = "Fichero No encontrado"
        
        # IT IS TO IMPORTANT TO CALL THIS METHOD HERE, BECAUSE AFTER CALL
        # ALL THE OTHER METHODS, THE WINDOWS NEEDS TO ENTER IN A INFINITE CICLE.
        self.__root.mainloop()

    def writeNumber(self, num):
        self.__selectedNumber.set(num)
    
    def showInfoSoftware(self):
        messagebox.showinfo("Bienvenido Usuario", "Este software esta en desarrollo, el primer modulo es una calculadora!")
        
    def showTextHelp(self):
        messagebox.showwarning("Peligro", "Usted  es digno de ayuda")
        
    def closeApplication(self):
        self.__optionCloseApp = messagebox.askquestion("Salir", "Deseas cerrar la applicacion")
        if (self.__optionCloseApp == "yes"):
            self.__root.destroy()
        else:
            print("Seguimos en el programa")
    
    def openFiles(self):
        # THE ATTRIBUTE , initialdir, LET US TO INDICATE IN WICH DIR WE WOULD LIKE TO BEGIN SERCHING THE FILE.
        self.__file = filedialog.askopenfilename(title="ABRE UN DOCUMENTO PARA EL PROYECTO DE PARADIGMAS", initialdir="C:")
                                            #     filetypes=(("Ficheros de Excel",".xlsx"),("Ficheros de texto",".txt"),("Todos lo ficheros",".*")))
        self.__fileName = path.basename(self.__file)
        print(self.__fileName)
              
    def initializeComponents(self):
        self.__root = Tk()
        self.__root.title("Paradigmas (Traductor)")
        self.__root.geometry("1000x550")
        self.__root.minsize(700, 300)
        self.__frame1 = Frame(self.__root, bg="white")
        self.__frame2 = Frame(self.__root, bg="white")
        
        self.__frame1.pack(side=LEFT, expand=TRUE, fill="both")
        self.__frame2.pack(side=RIGHT, expand=TRUE, fill="both")
        
    def addWidgetsLeftFrame(self):
        self.__cajalenguaje = Text(self.__frame1, width=80, height=33, bd=5, fg="blue", font=("Calibri", 12))
        self.__cajalenguaje.grid(row=1, column=0, padx=1, pady=1)
        
        # widgets de frame de  la derecha
        self.__frameRun = Frame(self.__frame2, bg="lightgray")
        self.__frameRun.grid(row=0, column=0, padx=10, pady=10, columnspan=4, sticky=W + E + N + S)
        
        self.__labelRun = Label(self.__frameRun, text="Run", font=('Arial', 12, 'bold', 'italic'), justify="center", width=6)
        self.__labelRun.grid(row=0, column=0, padx=5, pady=5, sticky=W + E + N + S)
        
        self.__cajatexto = Entry(self.__frameRun, width=40)
        self.__cajatexto.grid(row=1, column=0, columnspan=10, padx=5, pady=5, sticky=W + E + N + S)
        
        self.__botonRun = Button(self.__frameRun, text="Try", command=lambda:self.addStringToHistory(), font=('Arial', 12, 'bold', 'italic'))
        self.__botonRun.grid(row=2, column=0, padx=5, pady=5, sticky=W + E + N + S)
        
        self.__botonStep = Button(self.__frameRun, text="Steps", font=('Arial', 12, 'bold', 'italic'))
        self.__botonStep.grid(row=2, column=9, padx=5, pady=5, sticky=W + E + N + S)
        
        # widgets de frame de  history
        self.__frameHistorial = Frame(self.__frame2, bg="lightgray")
        self.__frameHistorial.grid(row=1, column=0, padx=10, pady=10, sticky=W + E + N + S)
        
        self.__labelhistory = Label(self.__frameHistorial, text="History", font=('Arial', 12, 'bold', 'italic'))
        self.__labelhistory.grid(row=0, column=0, padx=1, pady=1)
        
        self.__labelOcultarHistorial = Label(self.__frameHistorial, text="--", font=('Arial', 12, 'bold', 'italic'))
        self.__labelOcultarHistorial.grid(row=0, column=3, padx=1, pady=1)
        
        self.__historial = Text(self.__frameHistorial, width=38, height=15, bd=2)
        self.__historial.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
        
        # WE ADD A VERTICAL SCROLL TO OUR ETXT WIDGET.
        # self.__scrollHistory = Scrollbar(self.__historial,command=self.__historial.yview)
        # self.__scrollHistory.pack(expand=True,fill="both")
           
    def createMenu(self):
        self.__menuBar = Menu(self.__root)
        self.__root.config(menu=self.__menuBar)
        # ONCE WE HAVE CREATED OUR MENU, WE NEED TO ADD ITEMS TO OUR MENU, TEHN WE CALL TIS METHOD.
        self.addMenuItems()

    def addMenuItems(self):
        # tearoff=0,  THIS ATTRIBUTE IS TO AVOID SHOWING THE DEFAULT ITEM BAR IN OUR MENU ITEM.
        self.__archiveItemMenu = Menu(self.__menuBar, tearoff=0)
        self.__editItemMenu = Menu(self.__menuBar, tearoff=0)
        self.__toolsItemMenu = Menu(self.__menuBar, tearoff=0)
        self.__helpItemMenu = Menu(self.__menuBar, tearoff=0)
        self.__menuBar.add_cascade(label="Archivo", menu=self.__archiveItemMenu)
        self.__menuBar.add_cascade(label="Editar", menu=self.__editItemMenu)
        self.__menuBar.add_cascade(label="Herramientas", menu=self.__toolsItemMenu)
        self.__menuBar.add_cascade(label="Ayuda", menu=self.__helpItemMenu)
        
        # ONCE WE HAVE ADDED ITEMS TO OUR MENU, WE JUST NEED TO ADD OPCTION TO EACH MENU ITEM.
        # TEHN WE CALL THE METHOD BELOW
        self.addItemsMenuOptions()

    def addItemsMenuOptions(self):
        # WE AREA ADDING OPTIONS TO THE ITEM ARCHIVE
        self.__archiveItemMenu.add_command(label="Nuevo")
        self.__archiveItemMenu.add_command(label="Guardar", command=self.saveAlgorimth)
        self.__archiveItemMenu.add_command(label="Recuperar", command=self.loadAlgorimth)
        self.__archiveItemMenu.add_separator()
        self.__archiveItemMenu.add_command(label="Salir", command=self.closeApplication)
        
        # WE AREA ADDING OPTIONS TO THE ITEM EDIT
        self.__editItemMenu.add_command(label="Copiar")
        self.__editItemMenu.add_command(label="Pegar")
        self.__editItemMenu.add_command(label="Cortar")
        
        # WE AREA ADDING OPTIONS TO THE ITEM TOOLS
        self.__toolsItemMenu.add_command(label="Preferencias")
        self.__toolsItemMenu.add_command(label="Inicializar repositorio")
        self.__toolsItemMenu.add_command(label="Conectar con Git")
        
        # WE AREA ADDING OPTIONS TO THE ITEM HELP
        self.__helpItemMenu.add_command(label="Bienvenido")
        self.__helpItemMenu.add_command(label="Ver ayuda")
        self.__helpItemMenu.add_command(label="Sobre este software")

    def createAlgorimthFile(self):
        self.__archivo = open("algoritmo.txt", "w")
        self.__archivo.write("//Alfabeto\nL = {a, b}\n\n//Reglas\n \nab -> a\na -> b")
        self.__archivo.close()

    def createAuxAlgorimth(self):
        self.__archivo = open("algoritmo.txt", "a")
        for i in range(10) :
            self.__archivo.write("  " + str(i) + " " + "a" + "->" + "b\n")
        self.__archivo.close()

    def readDefaultAlgorimth(self):
        self.__texto = open("algoritmo.txt", "r")
        self.__lineas = self.__texto.readlines()
        
        for i in range(7):
            self.__cajalenguaje.insert(INSERT, self.__lineas[i])
        self.__texto.close()
        
    def saveAlgorimth(self):
        self.__archivo = open("algoritmo4.txt", "w")
        self.__archivo.write(self.__cajalenguaje.get(1.0, END))
        self.__archivo.close()

        # print(self.__cajalenguaje.get(1.0,END))
    def loadAlgorimth(self):
        self.__file = filedialog.askopenfilename(title="ABRE UN DOCUMENTO PARA EL PROYECTO DE PARADIGMAS", initialdir="C:")
        #filetypes=(("Ficheros de Excel",".xlsx"),("Ficheros de texto",".txt"),("Todos lo ficheros",".*")))
        self.__fileName = path.basename(self.__file)
        self.__archivo = open(self.__fileName, "r")
        self.__lineas = self.__archivo.readlines()
        # BEFORE ADDING NEW ALGORIMTH TO WIDGET TEXT, WE HAVE TO CLEAR THE TEXT IN THE WIDGET.
        self.__cajalenguaje.delete(1.0, END)
        for i in range(len(self.__lineas)):
            self.__cajalenguaje.insert(END, self.__lineas[i])
        self.__texto.close()
    
    def isAlfabeto(self, cadena):
        perteneceAlfabeto = True
        print(cadena)
        for i in range(len(cadena)):
            if(self.__lineas[1].__contains__(cadena[i])):
                print(perteneceAlfabeto)
                continue
            else:
                perteneceAlfabeto = False
        return perteneceAlfabeto
        
    def addStringToHistory(self):
        print(self.__lineas[1])
        if(self.isAlfabeto(self.__cajatexto.get())):
            self.__historial.insert(INSERT, "[" + str(len(self.__cajatexto.get())) + "] " + self.__cajatexto.get() + "\n")
        else:
            messagebox.showwarning("Esta palabra no corresponde al lenguaje utilizado!")
    
