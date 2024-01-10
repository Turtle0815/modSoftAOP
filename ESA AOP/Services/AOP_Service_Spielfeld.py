# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 17:12:54 2024

@author: schla
"""

import Layoutvorgaben.AOP_Spielfeld

def Spielfeld(Anwendung):
    Layoutvorgaben.AOP_Spielfeld.Spielfeld_Dimension(Anwendung)
    Layoutvorgaben.AOP_Spielfeld.Spielfeld_Beschriftung(Anwendung)
    
    Feld_x = 20
    Feld_y = 100
    
    a = 0
    for x in Layoutvorgaben.AOP_Spielfeld.Beschriftung_horizontal:      
        Feld_x = Feld_x + a*Layoutvorgaben.AOP_Spielfeld.Spielfeld_Dimension.Feld_Breite
        Feld_y = Feld_y + a*Layoutvorgaben.AOP_Spielfeld.Spielfeld_Dimension.Feld_Breite
    
    
        