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
        

# f) lage en egen funksjon for å skrive ut ei liste med kategorier inkludert indeks eller modifisere funksjonen for avtaler fra 
#  øving 9 slik at den også kan brukes for kategorier  

    def print_kategori(self):
        for a in self.kategori_list:
            t=0
            print(f"Indeks:{t}, Kategori: {self.kategori_list[t]}")
            t +=1
#--------------------------------------------------------------------------------------------

    
class Sted:
    def __init__(self, identifikasjon = None, navn = None, adresse = None):
        self.identifikasjon = identifikasjon
        self.navn = navn
        self.adresse = adresse
        self.sted_list = []
        
    def __str__(self):
        return f"{self.navn} med identifikasjon {self.identifikasjon} har adressen {self.adresse}"
    
    def nytt_sted(self):
        self.identifikasjon = input("Identifikasjon: ")
        self.navn = input("Navn: ")
        self.adresse = input("Adressen er: ")
        return Sted(self.identifikasjon, self.navn, self.adresse)
    
    def write_sted(self):
        with open("sted.txt", "a", encoding="UTF8") as fil:
            for a in self.sted_list:           
                fil.write(f"{a.identifikasjon};{a.navn};{a.adresse}\n")           
        print("Avtaler er skrevet inn i sted-fil")        
               

    def read_sted(self):
        with open("sted.txt", "r", encoding="UTF8") as fil:
            linje = fil.readline()
            while linje!="":                            
                linje = linje.split(";")
                identifikasjon = linje[0]
                navn = linje[1]
                adresse = linje[2]
                linje = fil.readline()                    
                self.sted_list.append(Sted(identifikasjon, navn, adresse)) 
                
"""
i) Enten lag funksjoner som lagrer og leser inn steder fra en egen sted-fil, eller utvid funksjonene fra øving 9 slik at de 
også lagrer og leser inn stedlista. Avgjør om stedene skal lagres i samme fil som avtalene eller i sin egen fil.
 

j) Enten sjekk funksjonen fra øving 9 oppgave g for å skrive ut alle avtaler om den også kan brukes for steder, 
    eller skriv en ny funksjon som skriver ut alle stedene i ei liste

#--------------------------------------------------------------------------------------------
"""    

if __name__ == "__main__":
    kategori = Kategori()
    kategori.ny_kategori()
    print(kategori)
    sted = Sted()
    sted.nytt_sted()
    print(sted)
    
   