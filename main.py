from appointmentmanager import AppointmentManager
from datetime import datetime

if __name__ == "__main__":
    # Initialise appointment manager
    manager = AppointmentManager()

    # Start by printing program title
    print("Avtaleboksystem:\n")

    # Infinite loop for command inputs
    while True:
        # Print command list
        print("Følgende kommandoer er tilgjengelige (skriv tall for å velge):\n")
        print("0: Les avtaler fra fil")
        print("1: Skriv avtaler til fil")
        print("2: Lag ny avtale")
        print("3: Avtaleliste")
        print("4: Slett avtale")
        print("5: Rediger avtale")
        print("6: Søk etter dato")
        print("7: Søk i tittel")
        print("8: Avslutt programmet")
        print()

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
            if not (0 <= command <= 8):
                print("Feil, input må være et heltall mellom 0 og 8 inklusivt.\n")
                command = None

        # Execute commands
        # Read
        if command == 0:
            manager.readAppointments()
            print("Fil innlest")
        # Write
        elif command == 1:
            manager.writeAppointments()
            print("Fil skrevet til")
        # Create
        elif command == 2:
            manager.newAppointment()
            print("Avtale laget")
        # List
        elif command == 3:
            manager.listAppointments("Tilgjengelige avtaler:")
        # Delete
        elif command == 4:
            manager.deleteAppointment()
        # Edit
        elif command == 5:
            manager.editAppointment()
        # Find by date
        elif command == 6:
            query = None
            while True:
                try:
                    query = datetime.fromisoformat(input("Sett inn en tid på formen ÅÅÅÅ-MM-DD TT:MM:SS: "))
                    break
                except ValueError:
                    print("Må være et tidsobjekt på formen ÅÅÅÅ-MM-DD TT:MM:SS")

            # Create a new manager to use print method
            mgr = AppointmentManager()

            mgr.appointments = manager.findAppointmentByDate(query)

            if len(mgr.appointments):
                mgr.listAppointments("Treff ved søk:")
            else:
                print("Ingen treff")
        # Find by keyword
        elif command == 7:
            # Create a new manager to use print method
            mgr = AppointmentManager()

            mgr.appointments = manager.findAppointmentByKeyword()

            if len(mgr.appointments):
                mgr.listAppointments("Treff ved søk:")
            else:
                print("Ingen treff")
        # Exit
        elif command == 8:
            break

        print()