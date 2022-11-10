#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 18:24:36 2022

@author: martefurnee
"""





class Kategori:
    def __init__(self, identifikasjon = None, navn = None, prioritet = 1):
        self.identifikasjon = identifikasjon
        self.navn = navn
        self.prioritet = prioritet
        

    def __str__(self):
        return f"{self.navn} med identifikasjon {self.identifikasjon} har prioritet nummer {self.prioritet}"
    
    def ny_kategori(self):
        self.identifikasjon = input("Identifikasjon: ")
        self.navn = input("Navn: ")
        self.prioritet = input("Prioritet nummer: ")
        return Kategori(self.identifikasjon, self.navn, self.prioritet)
        
        # if self.prioritet == 1:
        #     self.prioritet = "Vanlig"
        # elif self.prioritet == 2:
        #     self.prioritet = "Viktig"
        # elif self.prioritet == 3:
        #     self.prioritet = "Svært viktig"
        # else:
        #     print("Prioritet skal være et tall mellom 1 og 3")
        

    
class Sted:
    def __init__(self, identifikasjon = None, navn = None, adresse = None):
        self.identifikasjon = identifikasjon
        self.navn = navn
        self.adresse = adresse
        
    def __str__(self):
        return f"{self.navn} med identifikasjon {self.identifikasjon} har adressen {self.adresse}"
    
    def nytt_sted(self):
        self.identifikasjon = input("Identifikasjon: ")
        self.navn = input("Navn: ")
        self.adresse = input("Adressen er: ")
        return Sted(self.identifikasjon, self.navn, self.adresse)
        

if __name__ == "__main__":
    kategori = Kategori()
    kategori.ny_kategori()
    print(kategori)
    sted = Sted()
    sted.nytt_sted()
    print(sted)
    
   