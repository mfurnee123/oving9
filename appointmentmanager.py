from oving9_avtalebok import Avtale

class AppointmentManager:
    def __init__(self):
        self.appointments = []

    def __userIndex(self):
        """
        Gets an index for an appointment from user input from STDIN.

        :rtype int:
        :returns: An index within bounds for the self.appointments list.
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
        raise NotImplementedError

