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
        print("8: Søk etter sted")
        print("9: Lag nytt sted")
        print("10: Lag ny kategori")
        print("11: Avslutt programmet")
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
            if not (0 <= command <= 11):
                print("Feil, input må være et heltall mellom 0 og 11 inklusivt.\n")
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


            result = manager.findAppointmentByDate(query)

            if len(result):
                manager.printAppointments(result, "Treff ved søk:")
            else:
                print("Ingen treff")
        # Find by keyword
        elif command == 7:
            result = manager.findAppointmentByKeyword()

            if len(result):
                manager.printAppointments(result, "Treff ved søk:")
            else:
                print("Ingen treff")
        # Find by location
        elif command == 8:
            # Check that there are locations
            if not len(manager.location_list):
                print("Du har ingen steder")
                continue

            print("Tilgjengelige steder")
            manager.print_locations()

            # Print location list
            maxidx = len(manager.location_list) - 1

            print("Skriv inn indeksen til stedet du vil søke etter.")

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

            result = manager.findAppointmentByLocation(manager.location_list[idx])

            if len(result):
                manager.printAppointments(result, "Treff ved søk:")
            else:
                print("Ingen treff")
        # New location
        elif command == 9:
            manager.newLocation()
        # New category
        elif command == 10:
            manager.newCategory()
        # Exit
        elif command == 11:
            break

        print()