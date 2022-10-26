# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 08:43:54 2022

@author: USUARIO
"""

igv = 0.18

def obtenerIGVconSubtotal(subtotal):
    return subtotal*igv

def obtenerTotalconSubtotal(subtotal):
    # subtotal + igv*subtotal
    # subtotal * (1 + 0.18)
    return subtotal*(1 + igv)

def obtenerSubtotal(total):
    return total/(1 + igv)

def obtenerIGVTotal(total):
    return total - obtenerTotalconSubtotal(total)