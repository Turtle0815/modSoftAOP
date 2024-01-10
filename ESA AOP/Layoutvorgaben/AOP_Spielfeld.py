# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 16:39:55 2024

@author: schla
"""

horizontal =[3, 8]                         #[Index 0: TicTacToe, Index 1: Dame, Schach]
vertikal = [3, 8]                          #[Index 0: TicTacToe, Index 1: Dame, Schach]

Feld_Breite = [40, 40]                         #[Index 0: TicTacToe]
Feld_Hoehe = [40, 40]                          #[Index 0: TicTacToe]

Feld_x = [150, 150]                             #[Index 0: TicTacToe]
Feld_y = [150, 150]                             #[Index 0: TicTacToe]
 
def Spielfeld_Beschriftung(Anwendung): 
    global Index
    if Anwendung == 'TicTacToe':
        Index = 0
    if Anwendung == 'Schach':
        Index = 1     
