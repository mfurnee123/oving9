from oving9_avtalebok import Avtale

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

        # The ny_avtale method is an instance method of the Avtale class. This is not intuitive, and should preferably be moved here. 
        a = Avtale()

        a.ny_avtale()

        self.appointments.append(a)

    def readAppointments(self):
        raise NotImplementedError

    def writeAppointments(self):
        raise NotImplementedError

    def listAppointments(self, heading=None):
        raise NotImplementedError
    
    def editAppointment(self):
        raise NotImplementedError
    
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
       

