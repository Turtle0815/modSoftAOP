# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 14:49:52 2024

@author: schla
"""

import Schnittstellen.AOP_Schnittstelle_Titel

Zeilen = []
Spalten = []

def Labels_Position(GUI):
    global Label_a
    global Label_b
    
    if GUI == 'Wartung':
        Label_a = 100
        Label_b = 120           
            
def Labels_Dimension(GUI):
    global Label_Breite
    global Label_Hoehe
    
    if GUI == 'Wartung':
        Label_Breite = 200
        Label_Hoehe = 15

def Buttons_Position(GUI):
    global a
    global b
    
    if GUI== 'Hauptmenue':
        if len(Schnittstellen.AOP_Schnittstelle_Auswahl.Liste) < 9:
            a = 150
            b = 100
            for x in Schnittstellen.AOP_Schnittstelle_Auswahl.Liste:
                if (Schnittstellen.AOP_Schnittstelle_Auswahl.Liste.index(x)+1)%2 == 0:
                    Zeile = int((Schnittstellen.AOP_Schnittstelle_Auswahl.Liste.index(x)+1)/2)-1
                    Spalte = 1
                else:
                    Zeile = int((Schnittstellen.AOP_Schnittstelle_Auswahl.Liste.index(x)+2)/2)-1
                    Spalte = 0
                Zeilen.append (Zeile)
                Spalten.append (Spalte)
                
def Eingabefeld_Position():
    global x
    global y
    
    x = 100
    y = 50

def Button_Dimension(GUI):
    global Breite_Button
    global Hoehe_Button
    
    if GUI == 'Hauptmenue':
        if len(Schnittstellen.AOP_Schnittstelle_Auswahl.Liste) < 9:
            Breite_Button = 15
            Hoehe_Button = 2
            
    if GUI == 'Benutzereingabe':
        Breite_Button = 200
        Hoehe_Button = 30

def Faktoren(GUI):
    global Faktor_Zeilen
    global Faktor_Spalten
    
    if GUI== 'Hauptmenue':
        if len(Schnittstellen.AOP_Schnittstelle_Auswahl.Liste) < 9:
            Faktor_Zeilen = 125
            Faktor_Spalten = 425

def Fenster (GUI):
    global Geometrie
    
    global Breite
    global Hoehe
    
    if GUI == 'Passwort':
        GUI = 'Benutzereingabe'
    
    if GUI == 'Hauptmenue':
        Breite = '1000'
        Hoehe  = '600'
    
    if GUI == 'Benutzereingabe':
        Breite = '500'
        Hoehe = '250'
        
    Geometrie = Breite + 'x' + Hoehe  
    

            