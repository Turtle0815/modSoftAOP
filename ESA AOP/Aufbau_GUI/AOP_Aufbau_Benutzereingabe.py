# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 11:14:15 2024

@author: schla
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 14:44:44 2024

@author: schla
"""
import tkinter

import Layoutvorgaben.AOP_Geometrie                    # Vorgaben für die GUI-Geometrie
import Layoutvorgaben.AOP_Farben                       # Vorgaben für die farbliche Gestaltung der GUI
import Schnittstellen.AOP_Schnittstelle_Schrift        # Vorgaben für die Gestaltung der Schrift in den GUI
import Schnittstellen.AOP_Schnittstelle_Titel          # Vorgaben für Titel und Überschrift
import Services.AOP_Service_Benutzereingabe_einlesen   # liest Benutzereingaben ein und stellt sie als Variable zur Verfügung
import Services.AOP_Service_Fenster_schließen           


def Aufbau_Benutzereingabe(Zweck):
    
    GUI = 'Benutzereingabe'
    
    Layoutvorgaben.AOP_Geometrie.Fenster(GUI)
    
    Schnittstellen.AOP_Schnittstelle_Schrift.Schrift()
    Schnittstellen.AOP_Schnittstelle_Titel.Titel_festlegen(GUI)
    Schnittstellen.AOP_Schnittstelle_Titel.Ueberschrift_festlegen(GUI)
    Layoutvorgaben.AOP_Geometrie.Eingabefeld_Position()
    Layoutvorgaben.AOP_Geometrie.Button_Dimension(GUI)
    
    Fenster = tkinter.Tk()
    Fenster.title (Schnittstellen.AOP_Schnittstelle_Titel.Titel)
    Fenster.geometry (Layoutvorgaben.AOP_Geometrie.Geometrie)
    Fenster.configure (bg = Layoutvorgaben.AOP_Farben.Hintergrund_Fenster)
    Fenster.resizable (width = False, height = False)
    
    Ueberschrift = tkinter.Label (Fenster, text  = Schnittstellen.AOP_Schnittstelle_Titel.Ueberschrift, 
                                           font  = Schnittstellen.AOP_Schnittstelle_Schrift.Schrift_Ueberschrift_klein,
                                           bg    = Layoutvorgaben.AOP_Farben.Hintergrund_Label,
                                           fg    = Layoutvorgaben.AOP_Farben.Schriftfarbe_Label                                      
                                           )
    Ueberschrift.place (x = 0, y = 0, width = int(Layoutvorgaben.AOP_Geometrie.Breite))
    
    if Zweck == 'Passwort':
        show = '*'
    else:
        show = ''
        
    Eingabefeld = tkinter.Entry(Fenster, show = show)
    Eingabefeld.place (x = int(Layoutvorgaben.AOP_Geometrie.x),
                       y = int(Layoutvorgaben.AOP_Geometrie.y), 
                       height = 30, width = 300)
    
    Button_Eingabe_bestaetigen = tkinter.Button(Fenster, text='Eingabe bestätigen', 
                                                font = Schnittstellen.AOP_Schnittstelle_Schrift.Schrift_Button2,
                                                bg = Layoutvorgaben.AOP_Farben.Hintergrund_Button,
                                                fg = Layoutvorgaben.AOP_Farben.Schriftfarbe_Button,
                                                command = lambda: [Services.AOP_Service_Benutzereingabe_einlesen.Benutzereingabe_einlesen(Eingabefeld.get()), 
                                                                   Services.AOP_Service_Fenster_schließen.Fenster_schließen(Fenster)]
                                                )
    Button_Eingabe_bestaetigen.place (x = 200, y = 100, width = Layoutvorgaben.AOP_Geometrie.Breite_Button, 
                                                        height = Layoutvorgaben.AOP_Geometrie.Hoehe_Button,
                                                        )
    
    Fenster.mainloop()