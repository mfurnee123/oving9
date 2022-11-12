from oving9_avtalebok import Avtale
from datetime import datetime
from kategori_og_sted import Kategori, Sted

class AppointmentManager:
    def __init__(self):
        self.appointments = []
        self.locations = []
        self.categories = []
        
    def __userIndex(self, allowExit=True):
        """
        Gets an index for an appointment from user input from STDIN.
        :param bool allowExit: Whether the method should accept -1 as an input, intented for a special case, like exit.
        :rtype int:
        :returns: An index within bounds for the self.appointments list, or -1 if input by user and allowExit is true.
        """

        # Loop until a valid input is received
        idx = None

        while idx == None:
            raw = input(">")

            try:
                idx = int(raw)
            except:
                print("Feil, input må være et heltall.\n")
                idx = None
            
            # Special case for -1
            if idx == -1 and allowExit:
                return -1

            # Validate that the number is in the correct range
            if not (0 <= idx < len(self.appointments)):
                print(f"Feil, input må være et heltall mellom 0 og {len(self.appointments) - 1} inklusivt.\n")
                idx = None

        return idx

    def newAppointment(self):
        """
        Creates a new appointment from user input from STDIN.
        """
        a = Avtale()
        a.ny_avtale()              
        # The ny_avtale method is an instance method of the Avtale class. This is not intuitive, and should preferably be moved here.
        self.appointments.append(a)

    def readAppointments(self):
        with open("avtale_bok.txt", "r", encoding="UTF8") as fil:
            linje = fil.readline()
            while linje!="":                            
                linje = linje.split(";")
                tittel = linje[0]
                sted = linje[1]
                starttidspunkt = linje[2]
                try:
                    varighet = int(linje[3])
                except ValueError:
                    varighet = None
                linje = fil.readline()                    
                self.appointments.append(Avtale(tittel, sted, starttidspunkt, varighet))                     
    
 
       
    def writeAppointments(self):
        #open file in write mode
        with open("avtale_bok.txt", "a", encoding="UTF8") as fil:            
            for a in self.appointments:
                fil.write(f"{a.tittel};{a.starttidspunkt};{a.varighet};{a.sted}\n")           
        print("Avtaler er skrevet inn i Avtale-fil")        
                #En indeks på en linje                
              
        
    def findAppointmentByDate(self, dato):               
        dato = dato.date()        
        liste = self.appointments
        temp = []         
        for i in liste:
            if dato == i.starttidspunkt.date():
                temp.append(i)        
        return(temp)
    
    
    def findAppointmentByKeyword(self):
        kodeord = (input("Skriv tittel du ønsker å se avtaler til: "))
        temp = []
        for i in self.appointments:
            if kodeord.lower() in i.tittel.lower():
                temp.append(i)
        return(temp)        

        

    def printAppointments(self, appointments, heading=None):
        """
        Lists appointments in a given list.

        :param list appointments: A list of appointments to print.
        :param str heading: An optional heading to print.
        """
        if heading is not None: print(heading)

        # string padding
        pad = lambda x : x + (" " * (max(len("indeks"), len(str(len(appointments) - 1))) - len(x)))

        print(pad("Indeks"), "Avtale")

        print(*[f"{pad(str(i) + ':')} {appointments[i]}" for i in range(len(appointments))], sep="\n")

    def listAppointments(self, heading=None):
        """
        Lists all appointments in store.

        :param str heading: An optional heading to print.
        """
        return self.printAppointments(self.appointments, heading)
 
    def editAppointment(self):
        # Check if there are appointments
        if len(self.appointments) == 0:
            print("Du har ingen avtaler.")
            return
        
        # Print available appointments
        self.listAppointments("Avtaler tilgjengelige for redigering")

        print()
        print("Skriv inn indeksen til avtalen du ønsker å redigere, -1 for å gå tilbake.")
        print()

        idx = self.__userIndex()

        # Check for -1 exit code
        if idx == -1:
            return

        print("Valgt avtale:", self.appointments[idx])

        # New values
        newTitle = None
        newLocation = None
        newTime = None
        newDuration = None
            

        # Loop unit broken
        while True:
            print("Hva ønsker du å endre?")
            print("0: Tittel")
            print("1: Sted")
            print("2: Starttidspunkt")
            print("3: Varighet")
            print("4: Lagre")
            print("5: Avslutt uten å lagre")
            # Loop until a valid input is received
            command = None

            while command == None:
                raw = input(">")

                try:
                    command = int(raw)
                except:
                    print("Feil, input må være et heltall.\n")
                    command = None
                
                # Validate that the number is in the correct range
                if not (0 <= command <= 5):
                    print("Feil, input må være et heltall mellom 0 og 5 inklusivt.\n")
                    command = None
          

            # Saving
            if command == 4:
                if newTitle is not None:
                    self.appointments[idx].tittel = newTitle
                if newLocation is not None:
                    self.appointments[idx].sted = newLocation
                if newTime is not None:
                    self.appointments[idx].starttidspunkt = newTime
                if newDuration is not None:
                    self.appointments[idx].varighet = newDuration

                print("Avtale oppdatert.")
                return
            # Exit
            elif command == 5:
                print("Endringer forkastet.")
                return
            
            # Title
            elif command == 0:
                newTitle = input("Ny titel på avtalen: ")
            # Location
            elif command == 1:
                newLocation = input("Nytt sted til avtalen: ")
            # Time
            elif command == 2:
                while True:
                    try:
                        newTime = datetime.fromisoformat(input("Sett inn ny tid på formen ÅÅÅÅ-MM-DD TT:MM:SS: "))
                        break
                    except ValueError:
                        print("Må være et tidsobjekt på formen ÅÅÅÅ-MM-DD TT:MM:SS")
            # Duration
            elif command == 3:
                while True:
                    try:
                        newDuration = int(input("Varigheten i minutter til møtet (heltall): "))
                        break
                    except ValueError:
                        print("Må være et heltall")

            print()
            
        

    
    def deleteAppointment(self):
        # Check if there are appointments
        if len(self.appointments) == 0:
            print("Du har ingen avtaler.")
            return
        
        # Print available appointments
        self.listAppointments("Avtaler tilgjengelige for sletting")

        print()
        print("Skriv inn indeksen til avtalen du ønsker å slette, -1 for å gå tilbake.")
        print()

        idx = self.__userIndex()

        # Check for -1 exit code
        if idx == -1:
            return
        
        # Do the deletion
        print(f"Avtale {self.appointments.pop(idx)} slettet.\n")
        
   

    def newCategory(self):
        a = Kategori()
        a = a.ny_kategori()
        self.categories.append(a)
        
        
    def write_category(self):
        with open("kategori.txt", "a", encoding="UTF8") as fil:
            for a in self.categories:           
                fil.write(f"{a.identifikasjon};{a.navn};{a.prioritet}\n")           
        print("Avtaler er skrevet inn i Kategori-fil")                
               

    def read_category(self):
        with open("kategori.txt", "r", encoding="UTF8") as fil:
            linje = fil.readline()
            while linje!="":                            
                linje = linje.split(";")
                identifikasjon = linje[0]
                navn = linje[1]
                try:
                    prioritet = int(linje[2])
                except ValueError:
                    prioritet= None
                linje = fil.readline()                    
                self.categories.append(Kategori(identifikasjon, navn, prioritet))                     

    def print_categories(self):
        t=0
        for a in self.categories:           
            print(f"Indeks:{t}, Kategori: {a}")
            t +=1
 
    def new_location(self):
        a = Sted()
        a = a.nytt_sted()
        self.locations.append(a)
        
        
    def write_location(self):
        with open("sted.txt", "a", encoding="UTF8") as fil:
            for a in self.locations:           
                fil.write(f"{a.identifikasjon};{a.navn};{a.adresse}\n")           
        print("Avtaler er skrevet inn i sted-fil")        
               

    def read_locations(self):
        with open("sted.txt", "r", encoding="UTF8") as fil:
            linje = fil.readline()
            while linje!="":                            
                linje = linje.split(";")
                identifikasjon = linje[0]
                navn = linje[1]
                adresse = linje[2]
                linje = fil.readline()                    
                self.locations.append(Sted(identifikasjon, navn, adresse)) 
                

    def print_locations(self):
        for a in self.locations:           
            print(f"Sted: {a}")
            
  