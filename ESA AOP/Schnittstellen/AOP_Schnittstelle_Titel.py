# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 12:12:11 2023

@author: schla
"""

Titelliste = ['Spielesammlung', 'Maintenance', '']
Labelliste = ['Binders beste Bummelkiste', 'Wartungsziele:', 'Bitte geben Sie das Passwort ein:']

Wartungsliste = []

def Titel_festlegen (Anwendung):
    global Titel
    if Anwendung == 'Anwender':
        Titel = Titelliste[0]
    if Anwendung == 'Entwickler' or Anwendung == 'Wartung':
        Titel = Titelliste[1]
    if Anwendung == 'Benutzereingabe':
        Titel = Titelliste[2]
        
def Ueberschrift_festlegen (Anwendung):
    global Ueberschrift
    if Anwendung == 'Anwender':
        Ueberschrift = Labelliste[0]
    if Anwendung == 'Entwickler':
        Ueberschrift = Labelliste[1]
    if Anwendung == 'Benutzereingabe':
        Ueberschrift = Labelliste[2]

def Liste_uebergeben(Ziel):
    global Wartungsliste
    if Ziel == 'Titel':
        for Eintrag in Titelliste:
            Wartungsliste.append(Eintrag)
            

