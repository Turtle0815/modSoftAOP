# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 15:56:05 2024

@author: schla
"""

import tkinter
import string

import Layoutvorgaben.AOP_Geometrie                    # Vorgaben für die GUI-Geometrie
import Layoutvorgaben.AOP_Farben                       # Vorgaben für die farbliche Gestaltung der GUI
import Layoutvorgaben.AOP_Spielfeld
import Schnittstellen.AOP_Schnittstelle_Schrift        # Vorgaben für die Gestaltung der Schrift in den GUI
import Schnittstellen.AOP_Schnittstelle_Titel          # Vorgaben für Titel und Überschrift 
import Schnittstellen.AOP_Schnittstelle_Auswahl        # stellt die Möglichkeiten dür die Auswahl in der GUI bereit
import Schnittstellen.AOP_Schnittstelle_Button_Funktion
import Services.AOP_Service_Liste_Buttons  # stellt eine Liste der in der GUI erstellten Buttons zusammen
import Services.AOP_Service_Fenster_schließen

def Aufbau_Anwendung(Anwendung):
    
    if Anwendung == 'TicTacToe':
        Aufgabe = 'Spiel'
    
    GUI = 'Hauptmenue'
    
    Layoutvorgaben.AOP_Geometrie.Fenster(GUI)
    
    Schnittstellen.AOP_Schnittstelle_Schrift.Schrift()
    Schnittstellen.AOP_Schnittstelle_Titel.Titel_festlegen(GUI)
    
    Alphabet = []
    Alphabet =  list(string.ascii_uppercase)
       
    Beschriftung_horizontal = []
    Beschriftung_vertikal   = []
    
    Fenster = tkinter.Tk()
    Fenster.title (Schnittstellen.AOP_Schnittstelle_Titel.Titel)
    Fenster.geometry (Layoutvorgaben.AOP_Geometrie.Geometrie)
    Fenster.configure (bg = Layoutvorgaben.AOP_Farben.Hintergrund_Fenster)
    Fenster.resizable (width = False, height = False)
    
    Ueberschrift = tkinter.Label (Fenster, text  = Anwendung, 
                                           font  = Schnittstellen.AOP_Schnittstelle_Schrift.Schrift_Ueberschrift,
                                           bg    = Layoutvorgaben.AOP_Farben.Hintergrund_Label,
                                           fg    = Layoutvorgaben.AOP_Farben.Schriftfarbe_Label                                      
                                           )
    Ueberschrift.place (x = 0, y = 0, width = int(Layoutvorgaben.AOP_Geometrie.Breite))
     
    if Aufgabe == 'Spiel':
        Layoutvorgaben.AOP_Spielfeld.Spielfeld_Beschriftung(Anwendung)
        
        Index       = Layoutvorgaben.AOP_Spielfeld.Index
        Feld_x      = Layoutvorgaben.AOP_Spielfeld.Feld_x[Index]
        Feld_y      = Layoutvorgaben.AOP_Spielfeld.Feld_y[Index]
        Feld_Breite = Layoutvorgaben.AOP_Spielfeld.Feld_Breite[Index]
        Feld_Hoehe  = Layoutvorgaben.AOP_Spielfeld.Feld_Hoehe[Index]   
        horizontal  = Layoutvorgaben.AOP_Spielfeld.horizontal[Index]
        vertikal    = Layoutvorgaben.AOP_Spielfeld.vertikal[Index]
                
        Rahmen = tkinter.LabelFrame (borderwidth =2,
                                     relief = 'ridge',
                                     bg = '#00000B',
                                     )
        Rahmen.place (x = Feld_x,
                      y = Feld_y,                
                      width = Feld_Breite,
                      height = Feld_Hoehe,                 
                      )
        Label = tkinter.Label(Rahmen,
                              bg = '#BFEFFF',
                              width = Feld_Breite,
                              height = Feld_Hoehe,
                              )
        Label.pack(anchor='c')
        
        a = 0
        while a < horizontal:
            Beschriftung_horizontal.append(Alphabet[a])
            a = a + 1
        a = 0
        while a < vertikal:
            Beschriftung_vertikal.append(a + 1)
            a = a + 1
            
        b = 0 
        for x in Beschriftung_horizontal:
            Rahmen = tkinter.LabelFrame (borderwidth =2,
                                              relief = 'ridge',
                                                  bg = '#00000B',
                                         )
            Rahmen.place (x      = Feld_x + (b + 1) * Feld_Breite,
                          y      = Feld_y,                
                          width  = Feld_Breite,
                          height = Feld_Hoehe,                 
                              )
            Label = tkinter.Label(Rahmen,
                                  text   = x,
                                  bg     = '#BFEFFF',
                                  width  = Feld_Breite,
                                  height = Feld_Hoehe,
                                  )
            Label.pack(anchor='c')
            b = b + 1
            
        b = 0
        for x in Beschriftung_vertikal:
                Rahmen = tkinter.LabelFrame (borderwidth =2,
                                             relief = 'ridge',
                                             bg = '#00000B',
                                             )
                Rahmen.place (x = Feld_x,
                              y = Feld_y + (b + 1) *Feld_Hoehe,                
                              width = Feld_Breite,
                              height = Feld_Hoehe,                 
                              )
                Label = tkinter.Label(Rahmen,
                                      text = x,
                                      bg = '#BFEFFF',
                                      width = Feld_Breite,
                                      height = Feld_Hoehe,
                                      )
                Label.pack(anchor='c')
                b = b + 1
                
        a = 0 
        while a < horizontal:
            b = 0
            while b < vertikal:
                Rahmen = tkinter.LabelFrame (borderwidth = 2,
                                             relief      = 'ridge',
                                             bg          = '#00000B',
                                             )
                Rahmen.place (x      = Feld_x +  (a + 1) * Feld_Breite,
                              y      = Feld_y +  (b + 1) * Feld_Hoehe,                
                              width  = Feld_Breite,
                              height = Feld_Hoehe,                 
                              )
                Button = tkinter.Button(Rahmen,
                                        bg     = '#BFEFFF',
                                        width  = Feld_Breite,
                                        height = Feld_Hoehe,
                                        )
                Button.pack(anchor='c')
                Services.AOP_Service_Liste_Buttons.Liste_Buttons_erstellen(Button) 
                b = b + 1
            a = a + 1
                
                
    Fenster.mainloop()