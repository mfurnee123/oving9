from oving9_avtalebok import Avtale
from datetime import datetime
from kategori_og_sted import Sted, Kategori

class AppointmentManager:
    def __init__(self):
        self.appointments = []
        self.location_list = []
        self.category_list = []
        
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
        # Exit if no locations are present
        if not len(self.location_list):
            print("Du har ingen steder, lag sted først")
            return

        a = Avtale()

        a.tittel = input("Tittel på avtalen: ")
        
        print("Tilgjengelige steder")
        self.print_locations()

        # Print location list
        maxidx = len(self.location_list) - 1

        print("Skriv inn indeksen til stedet du vil bruke")

        # Loop until a valid input is received
        idx = None

        while idx == None:
            raw = input(">")

            try:
                idx = int(raw)
            except:
                print("Feil, input må være et heltall.\n")
                idx = None
            
            # Validate that the number is in the correct range
            if not (0 <= idx <= maxidx):
                print(f"Feil, input må være et heltall mellom 0 og {maxidx} inklusivt.\n")
                idx = None
        
        a.sted = self.location_list[idx]
      
        while True:
            try:
                a.starttidspunkt = datetime.fromisoformat(input("Sett inn en tid på formen ÅÅÅÅ-MM-DD TT:MM:SS: "))
                break
            except ValueError:
                print("Må være et tidsobjekt på formen ÅÅÅÅ-MM-DD TT:MM:SS")  
        
        while True:
            try:
                a.varighet = int(input("Varigheten i minutter til møtet (heltall): "))
                break
            except ValueError:
                print("Må være et heltall:")
               
        # The ny_avtale method is an instance method of the Avtale class. This is not intuitive, and should preferably be moved here.
        self.appointments.append(a)

    def readAppointments(self):
        # Start by reading categories and locations
        self.read_category()
        self.read_locations()

        with open("avtale_bok.txt", "r", encoding="UTF8") as fil:
            linje = fil.readline()
            while linje!="":                            
                linje = linje.split(";")
                tittel = linje[0]
                sted = self.location_list[int(linje[3])]
                starttidspunkt = datetime.fromisoformat(linje[1])
                try:
                    varighet = int(linje[2])
                except ValueError:
                    varighet = None

                a = Avtale(tittel, sted, starttidspunkt, varighet)

                for i in linje[4].strip().split(","):
                    try:
                        i = int(i)
                    except:
                        continue
                    a.addCategory(self.category_list[i])
                                    
                linje = fil.readline()                    
                self.appointments.append(a)                     
    
 
       
    def writeAppointments(self):
        # Start by saving categories and locations
        self.write_category()
        self.write_location()

        #open file in write mode
        with open("avtale_bok.txt", "a", encoding="UTF8") as fil:            
            for a in self.appointments:
                cat = map(self.category_list.index, a.categories)
                fil.write(f"{a.tittel};{a.starttidspunkt};{a.varighet};{self.location_list.index(a.sted)};{','.join(cat)}\n")           
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
        newCats = []
            

        # Loop unit broken
        while True:
            print("Hva ønsker du å endre?")
            print("0: Tittel")
            print("1: Sted")
            print("2: Starttidspunkt")
            print("3: Varighet")
            print("4: Legg til kategori")
            print("5: Lagre")
            print("6: Avslutt uten å lagre")
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
                if not (0 <= command <= 6):
                    print("Feil, input må være et heltall mellom 0 og 6 inklusivt.\n")
                    command = None
          

            # Saving
            if command == 5:
                if newTitle is not None:
                    self.appointments[idx].tittel = newTitle
                if newLocation is not None:
                    self.appointments[idx].sted = newLocation
                if newTime is not None:
                    self.appointments[idx].starttidspunkt = newTime
                if newDuration is not None:
                    self.appointments[idx].varighet = newDuration
                self.appointments[idx].categories += list(filter(lambda x : x not in self.appointments[idx].categories, newCats))

                print("Avtale oppdatert.")
                return
            # Exit
            elif command == 6:
                print("Endringer forkastet.")
                return
            
            # Title
            elif command == 0:
                newTitle = input("Ny titel på avtalen: ")
            # Location
            elif command == 1:
                print("Tilgjengelige steder")
                self.print_locations()

                # Print location list
                maxidx = len(self.location_list) - 1

                print("Skriv inn indeksen til stedet du vil bruke")

                # Loop until a valid input is received
                idx = None

                while idx == None:
                    raw = input(">")

                    try:
                        idx = int(raw)
                    except:
                        print("Feil, input må være et heltall.\n")
                        idx = None
                    
                    # Validate that the number is in the correct range
                    if not (0 <= idx <= maxidx):
                        print(f"Feil, input må være et heltall mellom 0 og {maxidx} inklusivt.\n")
                        idx = None
                
                newLocation = self.location_list[idx]
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
            # Category
            elif command == 4:
                if not len(self.category_list):
                    print("Du har ingen kategorier")
                    continue

                print("Tilgjengelige kategorier:")
                self.print_categories()

                maxidx = len(self.category_list) - 1

                print("Skriv inn indeksen til kategorien du vil legge til.")

                # Loop until a valid input is received
                catidx = None

                while catidx == None:
                    raw = input(">")

                    try:
                        catidx = int(raw)
                    except:
                        print("Feil, input må være et heltall.\n")
                        catidx = None
                    
                    # Validate that the number is in the correct range
                    if not (0 <= catidx <= maxidx):
                        print(f"Feil, input må være et heltall mellom 0 og {maxidx} inklusivt.\n")
                        catidx = None

                newCats.append(self.category_list[catidx])


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
        """
        Creates a new category from user input and saves it to the hash map.
        """
        k = Kategori()
        n = k.ny_kategori()
        self.category_list.append(n)
        
    def write_category(self):
        with open("kategori.txt", "a", encoding="UTF8") as fil:
            for a in self.category_list:           
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
                self.category_list.append(Kategori(identifikasjon, navn, prioritet))                     

    def print_categories(self):
        t=0
        for a in self.category_list:           
            print(f"Indeks:{t}, Kategori: {a}")
            t +=1        
        


    def newLocation(self):
        """
        Creates a new location from user input and saves it to the hash map.
        """
        l = Sted()

        n = l.nytt_sted()
        self.location_list.append(n)
        
    def write_location(self):
        with open("sted.txt", "a", encoding="UTF8") as fil:
            for a in self.location_list:           
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
                self.location_list.append(Sted(identifikasjon, navn, adresse)) 
                
    def print_locations(self):
        # string padding
        pad = lambda x : x + (" " * (max(len("indeks"), len(str(len(self.location_list) - 1))) - len(x)))

        print(pad("Indeks"), "Sted")

        print(*[f"{pad(str(i) + ':')} {self.location_list[i]}" for i in range(len(self.location_list))], sep="\n")

            

    def findAppointmentByLocation(self, location):
        """
        Finds all appointments where the location identificator matches.

        :param Sted location: The location to look for.
        :rtype list:
        :returns: A list of all appointments a the specific location.
        """

        return list(filter(lambda x : x.sted.identifikasjon == location.identifikasjon, self.appointments))
  