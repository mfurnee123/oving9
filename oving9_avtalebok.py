#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 15:10:42 2022

@author: martefurnee
"""

class Avtale:
    def __init__(self, tittel, sted, starttidspunkt, varighet):
        self.tittel = tittel
        self.sted = sted
        self.startttidspunkt = starttidspunkt
        self.varighet = varighet
    
        
    def __str__(self):
        return f"Du har en avtale {self.tittel} kl.{self.starttidspunkt} som varer i {self.varighet}, sted: {self.sted}"
        