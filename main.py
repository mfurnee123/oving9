from appointmentmanager import AppointmentManager

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
        print("6: Avslutt programmet")
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
            if not (0 <= command <= 6):
                print("Feil, input må være et heltall mellom 0 og 6 inklusivt.\n")
                command = None

        # Execute commands
        # Read
        if command == 0:
            manager.readAppointments()
        # Write
        elif command == 1:
            manager.writeAppointments()
        # Create
        elif command == 2:
            manager.newAppointment()
        # List
        elif command == 3:
            manager.listAppointments()
        # Delete
        elif command == 4:
            manager.deleteAppointment()
        # Edit
        elif command == 5:
            manager.editAppointment()
        # Exit
        elif command == 6:
            break

        print()