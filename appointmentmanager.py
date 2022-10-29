from oving9_avtalebok import Avtale
from datetime import datetime

class AppointmentManager:
    def __init__(self):
        self.appointments = []

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
#i
    def readAppointments(self):
        avtale_fil = []
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
                avtale_fil.append(Avtale(tittel, sted, starttidspunkt, varighet))                     
        return avtale_fil     
 
#ok       
    def writeAppointments(self):
        #open file in write mode
        with open("avtale_bok.txt", "a", encoding="UTF8") as fil:            
            for a in self.appointments:
                fil.write(f"{a.tittel};{a.starttidspunkt};{a.varighet};{a.sted}\n")           
        print("Avtaler er skrevet inn i Avtale-fil")        
                #En indeks på en linje                

                
#ok        
    def findAppointmentByDate(self, dato_input=None):        
        if dato_input == None:
            dato_input = input("Skriv inn dato du ønsker å se avtaler til på formen ÅÅÅÅ-MM-DD: ")        
        liste = self.readAppointments()
        temp = []         
        for i in liste:
            test = i.starttidspunkt
            test= test.split()
            dato = test[0]
            if dato_input == dato:
                temp.append(i)        
        return(temp)


    def listAppointments(self, heading=None):
        raise NotImplementedError
 
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
       

