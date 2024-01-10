# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 13:50:24 2024

@author: schla
"""

import Aufbau_GUI.AOP_Aufbau_Wartung
import Aufbau_GUI.AOP_Aufbau_Anwendung

def Auswahl_ausfuehren(Anforderer, x):
    if Anforderer == 'Entwickler':
        Aufbau_GUI.AOP_Aufbau_Wartung.Aufbau_Wartung(x)
    if Anforderer == 'Anwender':
        Aufbau_GUI.AOP_Aufbau_Anwendung.Aufbau_Anwendung(x)