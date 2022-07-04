import sys
import os

from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6 import uic
from tkinter import messagebox

class Dialogo (QDialog):
    def __init__(self):
        ruta = os.path.dirname (os.path.abspath (__file__)) + r"\..\vista\EditarAsignatura.ui"
        QDialog.__init__ (self)
        uic.loadUi (ruta, self)

        self.pbGuardar.clicked.connect (self.guardar)
        self.pbCancelar.clicked.connect (self.cerrar)

    def guardar(self):
        pass
        '''if len (nombreAsignatura) == 0:
            return False
        busqueda = session.query (Asignatura).filter (Asignatura.nombreAsignatura == nombreAsignatura).all ()
        if len (busqueda) == 0:
            asignatura = session.query (Asignatura).filter (Asignatura.idAsignatura == idAsignatura).first ()
            asignatura.nombreAsignatura = nombreAsignatura
            session.commit ()
            return True
        else:
            return False
        '''

    def cerrar(self):
        resultado = messagebox.askquestion ("Salir", "¿Está seguro que desea salir?")
        if resultado == "yes":
            # exit(0)
            quit (0)

if __name__ == '__main__':
    app = QApplication (sys.argv)
    dialogo = Dialogo ()
    dialogo.show ()
    app.exec ()