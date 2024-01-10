# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:09:45 2024

@author: schla
"""

import tkinter

import Layoutvorgaben.AOP_Geometrie                     # Vorgaben für die GUI-Geometrie
import Layoutvorgaben.AOP_Farben                        # Vorgaben für die farbliche Gestaltung der GUI
import Schnittstellen.AOP_Schnittstelle_Schrift         # Vorgaben für die Gestaltung der Schrift in den GUI
import Schnittstellen.AOP_Schnittstelle_Titel           # Vorgaben für Titel und Überschrift 
import Schnittstellen.AOP_Schnittstelle_Auswahl         # stellt die Möglichkeiten dür die Auswahl in der GUI bereit
import Schnittstellen.AOP_Schnittstelle_Button_Funktion #übernimmt die Auswahl des Anwenders und baut die entsprechende GUI auf.
import Services.AOP_Service_Liste_Buttons               # stellt eine Liste der in der GUI erstellten Buttons zusammen
import Services.AOP_Service_Fenster_schließen

def Aufbau_Wartung(Ziel):
    
    GUI = 'Wartung'
    
    Layoutvorgaben.AOP_Geometrie.Fenster(GUI)
    
    Schnittstellen.AOP_Schnittstelle_Schrift.Schrift()
    Schnittstellen.AOP_Schnittstelle_Titel.Titel_festlegen(GUI)
    
    Fenster = tkinter.Tk()
    Fenster.title (Schnittstellen.AOP_Schnittstelle_Titel.Titel)
    Fenster.geometry (Layoutvorgaben.AOP_Geometrie.Geometrie)
    Fenster.configure (bg = Layoutvorgaben.AOP_Farben.Hintergrund_Fenster)
    Fenster.resizable (width = False, height = False)
    
    Ueberschrift = tkinter.Label (Fenster, text  = 'Wartungsziel: ' + Ziel, 
                                           font  = Schnittstellen.AOP_Schnittstelle_Schrift.Schrift_Ueberschrift,
                                           bg    = Layoutvorgaben.AOP_Farben.Hintergrund_Label,
                                           fg    = Layoutvorgaben.AOP_Farben.Schriftfarbe_Label                                      
                                           )
    Ueberschrift.place (x = 0, y = 0, width = int(Layoutvorgaben.AOP_Geometrie.Breite))
    
    Label1 = tkinter.Label (Fenster, text = 'Derzeitige Einträge:',
                                     font = Schnittstellen.AOP_Schnittstelle_Schrift.Schrift_Ueberschrift_klein, 
                                     bg   = Layoutvorgaben.AOP_Farben.Hintergrund_Label,
                                     fg   = Layoutvorgaben.AOP_Farben.Schriftfarbe_Label)
    Label1.place (x = 75, y = 60)
    
    Schnittstellen.AOP_Schnittstelle_Titel.Liste_uebergeben(Ziel)
    b = 0
    for Eintrag in Schnittstellen.AOP_Schnittstelle_Titel.Wartungsliste:
        Layoutvorgaben.AOP_Geometrie.Labels_Position(GUI)
        Layoutvorgaben.AOP_Geometrie.Labels_Dimension(GUI)
        
        Label_Ziel = tkinter.Label (Fenster, text   = '"' + Eintrag + '"',
                                             font   = Schnittstellen.AOP_Schnittstelle_Schrift.Schrift_Text,
                                             bg     = Layoutvorgaben.AOP_Farben.Hintergrund_Label,
                                             fg     = Layoutvorgaben.AOP_Farben.Schriftfarbe_Label,
                                             anchor = 'w',
                                             )
        Label_Ziel.place (x = Layoutvorgaben.AOP_Geometrie.Label_a,
                          y = Layoutvorgaben.AOP_Geometrie.Label_b + b,
                          width = int(Layoutvorgaben.AOP_Geometrie.Label_Breite),
                          )
        b = b + 60
        
    b = 0
    for Eintrag in Schnittstellen.AOP_Schnittstelle_Titel.Wartungsliste:
        links = 400
        oben = 115
        
        Button_aendern = tkinter.Button (Fenster, text   = 'ändern',
                                             font   = Schnittstellen.AOP_Schnittstelle_Schrift.Schrift_Button2,
                                             bg     = Layoutvorgaben.AOP_Farben.Hintergrund_Button,
                                             fg     = Layoutvorgaben.AOP_Farben.Schriftfarbe_Button,
                                             )
        Button_aendern.place (x = links,
                              y = oben + b,
                              width = int(Layoutvorgaben.AOP_Geometrie.Label_Breite),
                              )
        b = b + 55      
    
    Fenster.mainloop()