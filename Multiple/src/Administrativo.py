# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Andres Aquin"
__date__ = "$18-04-2021 01:19:17 AM$"

from Persona import Persona
class Administrativo(Persona):
    def __init__(self, item, fechaIngreso):
        self.item=item
        self.fechaIngreso=fechaIngreso
        
    def leer(self):
        print("Item: ")
        i=input()
        self.item=i
        print("Fecha de Ingreso: ")
        self.fechaIngreso=input()   #es el mismo metodo, pero diferente manera
        
    def mostrar(self):
        print("Item. "+str(self.item))
        print("Fecha de ingreso: "+self.fechaIngreso)
    
    def nombre(self):
        print("gana Administrativo")
        