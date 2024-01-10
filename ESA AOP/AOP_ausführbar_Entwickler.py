# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:09:26 2024

@author: schla
"""

import Aufbau_GUI.AOP_Aufbau_Benutzereingabe
import Aufbau_GUI.AOP_Aufbau_Hauptmenue

import Services.AOP_Service_Benutzereingabe_einlesen

Index_Benutzereingabe = 'Passwort'

Aufbau_GUI.AOP_Aufbau_Benutzereingabe.Aufbau_Benutzereingabe(Index_Benutzereingabe,    
                                                             )

Index_Hauptmenue = 'Entwickler'

if Services.AOP_Service_Benutzereingabe_einlesen.Benutzereingabe == '1234':
    
    Aufbau_GUI.AOP_Aufbau_Hauptmenue.Aufbau_Hauptmenue(Index_Hauptmenue,
                                                       )