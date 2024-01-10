# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 16:37:57 2024

@author: schla
"""

Anwender = ['TicTacToe', 'Schach', 'Dame']
Entwickler = ['Titel', 'Anwendungsliste', 'Geometrie']

Liste = []

def Auswahl (Anforderer):
    global Liste
    if Anforderer == 'Anwender':
        a = 0
        while a < len(Anwender):
            Liste.append(Anwender[a])
            a = a + 1
    if Anforderer == 'Entwickler':
        a = 0
        while a < len(Entwickler):
            Liste.append(Entwickler[a])
            a = a + 1