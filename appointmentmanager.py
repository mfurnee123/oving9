from oving9_avtalebok import Avtale

class AppointmentManager:
    def __init__(self):
        self.appointments = []

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

