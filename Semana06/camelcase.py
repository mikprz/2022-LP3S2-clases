# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 09:23:06 2022

@author: USUARIO
"""

import camelcase
nombre = "Miguel Angel Prado Zuta"
print(nombre.upper())
print(nombre.title())

cam = camelcase.CamelCase()
print("Con camelcase...")

# Imprimimos el nombre en formato titulo
# Utiizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema, creamos otro objeto, incluimos los argumentos
# 'Miguel' y 'Nicole'
cam2 = camelcase.CamelCase('Miguel','Nicole')