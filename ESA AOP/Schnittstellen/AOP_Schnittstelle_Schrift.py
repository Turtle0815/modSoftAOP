# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:38:49 2024

@author: schla
"""

def Schrift():  
    global Schrift_Ueberschrift
    global Schrift_Ueberschrift_klein
    global Schrift_Button1                                   # große Buttons, z.B. Hauptmenü mit weniger als 9 Einträgen
    global Schrift_Button2                                   # kleine Buttons, z.B. Eingabe bestätigen
    global Schrift_Text
    
    global Schriftart
    global Schriftstil
    global Schriftgroeße_Ueberschrift
    global Schriftgroeße_Button1
    global Schriftgroeße_Button2
    
    Schriftart = 'Verdana'
    
    Schriftgroeße_25 = '25'
    Schriftgroeße_20 = '20'
    Schriftgroeße_15 = '15'
    Schriftgroeße_10 = '10'
    
    Schriftstil_fett = 'bold'
    Schriftstil_normal = ''
                 
    Schrift_Ueberschrift       = Schriftart + ' ' + Schriftgroeße_25 + ' ' + Schriftstil_fett
    Schrift_Ueberschrift_klein = Schriftart + ' ' + Schriftgroeße_15 + ' ' + Schriftstil_fett
    Schrift_Button1            = Schriftart + ' ' + Schriftgroeße_20 + ' ' + Schriftstil_fett
    Schrift_Button2            = Schriftart + ' ' + Schriftgroeße_15 + ' ' + Schriftstil_normal
    Schrift_Text               = Schriftart + '' + Schriftgroeße_15 + '' + Schriftstil_normal
    