# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Andres Aquin"
__date__ = "$18-04-2021 01:18:51 AM$"

from Persona import Persona
class Docente(Persona):
    def __init__(self, categoria, tipo):
        self.categoria=categoria
        self.tipo=tipo
    
    def getCategoria(self):
        return self.categoria
    
    def getTipo(self):
        return self.tipo
    
    def setCategoria(self, c):
        self.categoria=c
        
    def setTipo(self, t):
        self.tipo=t
        
    def leer(self):
        self.setCategoria(input("Categoria: "))
        print("Tipo: ")
        tip=input()
        self.setTipo(tip) #es el mismo metodo que categoria solo que más largo
        
    def mostrar(self):
        print("Categoria: "+self.getCategoria())
        print("Tipo: "+self.tipo)
        
    def nombre(self):
        print("gana Docente")
        