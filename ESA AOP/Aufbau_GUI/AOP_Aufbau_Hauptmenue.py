# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 14:44:44 2024

@author: schla
"""
import tkinter

import Layoutvorgaben.AOP_Geometrie                     # Vorgaben für die GUI-Geometrie
import Layoutvorgaben.AOP_Farben                        # Vorgaben für die farbliche Gestaltung der GUI
import Schnittstellen.AOP_Schnittstelle_Schrift         # Vorgaben für die Gestaltung der Schrift in den GUI
import Schnittstellen.AOP_Schnittstelle_Titel           # Vorgaben für Titel und Überschrift 
import Schnittstellen.AOP_Schnittstelle_Auswahl         # stellt die Möglichkeiten dür die Auswahl in der GUI bereit
import Schnittstellen.AOP_Schnittstelle_Button_Funktion # übernimmt die Auswahl des Anwenders und baut die entsprechende GUI auf.
import Services.AOP_Service_Liste_Buttons               # stellt eine Liste der in der GUI erstellten Buttons zusammen
import Services.AOP_Service_Fenster_schließen

def Aufbau_Hauptmenue(Anforderer):
    
    GUI = 'Hauptmenue'
    
    Layoutvorgaben.AOP_Geometrie.Fenster(GUI)
    
    Schnittstellen.AOP_Schnittstelle_Schrift.Schrift()
    Schnittstellen.AOP_Schnittstelle_Titel.Titel_festlegen(Anforderer)
    Schnittstellen.AOP_Schnittstelle_Titel.Ueberschrift_festlegen(Anforderer)
    Schnittstellen.AOP_Schnittstelle_Auswahl.Auswahl(Anforderer)
    
    Fenster = tkinter.Tk()
    Fenster.title (Schnittstellen.AOP_Schnittstelle_Titel.Titel)
    Fenster.geometry (Layoutvorgaben.AOP_Geometrie.Geometrie)
    Fenster.configure (bg = Layoutvorgaben.AOP_Farben.Hintergrund_Fenster)
    Fenster.resizable (width = False, height = False)
    
    Ueberschrift = tkinter.Label (Fenster, text  = Schnittstellen.AOP_Schnittstelle_Titel.Ueberschrift, 
                                           font  = Schnittstellen.AOP_Schnittstelle_Schrift.Schrift_Ueberschrift,
                                           bg    = Layoutvorgaben.AOP_Farben.Hintergrund_Label,
                                           fg    = Layoutvorgaben.AOP_Farben.Schriftfarbe_Label                                      
                                           )
    Ueberschrift.place (x = 0, y = 0, width = int(Layoutvorgaben.AOP_Geometrie.Breite))
    
    Position = 0
    for x in Schnittstellen.AOP_Schnittstelle_Auswahl.Liste:
        Layoutvorgaben.AOP_Geometrie.Buttons_Position(GUI)
        Layoutvorgaben.AOP_Geometrie.Button_Dimension(GUI)
        Layoutvorgaben.AOP_Geometrie.Faktoren(GUI)
        
        Spalte = Layoutvorgaben.AOP_Geometrie.Spalten[Position]
        Zeile  = Layoutvorgaben.AOP_Geometrie.Zeilen[Position]
        
        Button = tkinter.Button(Fenster, text   = x,
                                         font   = Schnittstellen.AOP_Schnittstelle_Schrift.Schrift_Button1,
                                         bg     = Layoutvorgaben.AOP_Farben.Hintergrund_Button,
                                         fg     = Layoutvorgaben.AOP_Farben.Schriftfarbe_Button,
                                         width  = Layoutvorgaben.AOP_Geometrie.Breite_Button,
                                         height = Layoutvorgaben.AOP_Geometrie.Hoehe_Button,
                                         )
        Button.place (x = Layoutvorgaben.AOP_Geometrie.a
                      + Spalte*Layoutvorgaben.AOP_Geometrie.Faktor_Spalten,
                      y = Layoutvorgaben.AOP_Geometrie.b
                      + Zeile*Layoutvorgaben.AOP_Geometrie.Faktor_Zeilen)
        
        Services.AOP_Service_Liste_Buttons.Liste_Buttons_erstellen(Button) 
        
        Services.AOP_Service_Liste_Buttons.Liste_Buttons[-1]['command'] = lambda x=Services.AOP_Service_Liste_Buttons.Liste_Buttons[-1].cget('text'): [Services.AOP_Service_Fenster_schließen.Fenster_schließen(Fenster), 
                                                                                                                                                       Schnittstellen.AOP_Schnittstelle_Button_Funktion.Auswahl_ausfuehren(Anforderer, x),                                                                                                                                                      ]
        Position = Position + 1
    
    Fenster.mainloop()