#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 15:10:42 2022

@author: amskje
"""

class Avtale:
    def __init__(self, tittel=None, sted=None, starttidspunkt=None, varighet=None):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet
        self.categories = []
        
    def __str__(self):
        return f"Du har en avtale {self.tittel} kl.{self.starttidspunkt} som varer i {self.varighet}min, sted: {self.sted}"
    
    def addCategory(self, category):
        """
        Appends a category to the appointment.

        :param Kategori category: The category to append to the appointment.
        """

        self.categories.append(category)
     
        
if __name__ == "__main__":   
    avtale = Avtale()
    avtale.ny_avtale()
    print(avtale)