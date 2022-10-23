#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 15:10:42 2022

@author: martefurnee
"""

from datetime import datetime

class Avtale:
    def __init__(self, tittel=None, sted=None, starttidspunkt=None, varighet=None):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet
        
    def __str__(self):
        return f"Du har en avtale {self.tittel} kl.{self.starttidspunkt} som varer i {self.varighet}, sted: {self.sted}"
        
    
    def ny_avtale(self):
        self.tittel = input("Tittel på avtalen: ")
        self.sted = input("Sted: ")
        self.starttidspunkt = input("Avtalen starter: ")
        self.varighet = input("Avtalen varer: ")
        return self.tittel, self.sted, self.starttidspunkt, self.varighet
        
        
        
        
        
        


if __name__ == "__main__":   
    avtale = Avtale()
    avtale.ny_avtale()
    print(avtale)
    