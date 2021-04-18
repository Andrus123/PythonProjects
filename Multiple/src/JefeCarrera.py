# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Andrés Aquin"
__date__ = "$18-04-2021 01:19:40 AM$"

from Administrativo import Administrativo
from Docente import Docente
class JefeCarrera(Docente, Administrativo):
    def __init__(self, categoria, tipo, item, fechaIngreso, unidad):
        Docente.__init__(self, categoria, tipo)
        Administrativo.__init__(self, item, fechaIngreso)
        self.unidad=unidad
        
    def getUnidad(self):
        return self.unidad
    
    def setUnidad(self, unidad):
        self.unidad=unidad
        
    def leer(self):
        Docente.leer(self)
        Administrativo.leer(self)
        print("Unidad: ")
        u=input()
        self.setUnidad(u)
        
    def mostrar(self):
        Docente.mostrar(self)
        Administrativo.mostrar(self)
        print("Unidad: ", self.unidad)
        
    
