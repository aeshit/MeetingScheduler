from database.in_memory_database import InMemoryDatabase
from models.calendar_owner import CalendarOwner
from models.invitee import Invitee
from models.availability_rule import AvailabilityRule
from utils.utils import convert_to_24_hour, generate_uuid  # Utility for converting time to 24-hour format


############################################################
# Command Line Interface
# This section provides an interactive CLI for managing calendar owners,
# invitees, and scheduling operations.

def create_calendar_owner(name, availability_rule):
    """
    Create a new calendar owner with a given name and availability rule.
    """
    return CalendarOwner(name, availability_rule, generate_uuid())

def create_invitee(name, calendar_owner):
    """
    Create a new invitee associated with a specific calendar owner.
    """
    return Invitee(name, calendar_owner)

def CLIInterface():
    """
    Main CLI interface for managing calendar scheduling.
    """
    # Initialize lists for calendar owners and invitees
    noOfOwners = int(input("Enter number of Calendar owners: "))
    noOfInvitees = int(input("Enter number of Invitees: "))
    owners = []
    invitees = []
    
    # Collect data for calendar owners
    print("Creating calendar owners...")
    for i in range(noOfOwners):
        owner_name = input(f"Enter name for calendar owner {i + 1}: ")
        availability_rule = AvailabilityRule(
            start_hour=int(convert_to_24_hour(input(f"Enter start hour for {owner_name}'s availability (1 PM, or 13): "))),
            end_hour=int(convert_to_24_hour(input(f"Enter end hour for {owner_name}'s availability (1 PM, or 13): "))),
            days_of_week=set(input(f"Enter days of week for {owner_name} (comma separated, e.g., Monday,Tuesday): ").split(","))
        )
        owners.append(create_calendar_owner(owner_name, availability_rule))
    
    # Collect data for invitees
    print("Creating invitees...")
    for i in range(noOfInvitees):
        invitee_name = input(f"Enter name for invitee {i + 1}: ")
        owner_idx = int(input(f"Select a calendar owner for {invitee_name} (1-{noOfOwners}): ")) - 1
        invitees.append(create_invitee(invitee_name, owners[owner_idx]))
    
    # Command options for scheduling operations
    while True:
        print("\nSelect an action:")
        print("1. Search available slots")
        print("2. Book a slot")
        print("3. List appointments")
        print("4. Exit")
        
        action = input("Enter your choice: ")

        if action == "1":
            # Search available slots for an invitee
            invitee_name = input("Enter your name: ")
            invitee = next(i for i in invitees if i.name == invitee_name)
            available_slots = invitee.search_available_slots()
            if available_slots:
                print("Available slots:")
                for slot in available_slots:
                    print(slot)
            else:
                print("No available slots.")
        
        elif action == "2":
            # Book a time slot for an invitee
            invitee_name = input("Enter your name: ")
            invitee = next(i for i in invitees if i.name == invitee_name)
            date = input("Enter the date (e.g., 2024-12-31): ")
            day = input("Enter the day (e.g., Monday): ")
            start_time = input("Enter start time (e.g., 9 AM or 14): ")
            end_time = input("Enter end time (e.g., 10 AM or 15): ")
            result = invitee.book_slot(date, start_time, end_time, day)
            print(result)
        
        elif action == "3":
            # List appointments for a calendar owner
            owner_name = input("Enter calendar owner's name: ")
            owner_class = None
            for owner in owners:
                if owner.name == owner_name:
                    owner_class = owner
            appointments = owner_class.list_appointments()
            if appointments:
                for appointment in appointments:
                    print(appointment)
            else:
                print("No appointments found.")
        
        elif action == "4":
            # Exit the CLI
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


############################################################
if __name__ == "__main__":
    # Example main function to demonstrate functionality
    
    # Run with this for CLI
    # main()

    # Initialize the singleton InMemoryDatabase instance
    db = InMemoryDatabase.get_instance()

    # Create calendar owners and add them to the database
    owner1 = CalendarOwner("John Doe",AvailabilityRule(),"123")
    owner2 = CalendarOwner("Jane Smith",AvailabilityRule(),"456")
    db.add_calendar_owner(owner1.id, owner1)
    db.add_calendar_owner(owner2.id, owner2)

    # Set up availability rules for each owner
    owner1.setup_availability("10 AM", "5 PM", {"Monday", "Wednesday", "Friday"})
    owner2.setup_availability("9 AM", "4 PM", {"Tuesday", "Thursday"})

    # Create invitees and associate them with calendar owners
    invitee1 = Invitee("Alice", owner1)
    invitee2 = Invitee("Bob", owner2)
    invitee3 = Invitee("Charlie", owner1)
    invitee4 = Invitee("Diana", owner2)
    invitee5 = Invitee("Eve", owner1)

    # Add invitees to the respective calendar owners
    owner1.add_invitee(invitee1)
    owner1.add_invitee(invitee3)
    owner1.add_invitee(invitee5)
    owner2.add_invitee(invitee2)
    owner2.add_invitee(invitee4)

    # Example operations: Updating availability, searching, booking, and listing appointments
    print("\n--- Owner2 (Jane Smith) updating her availability rule ---")
    owner2.availability_rule.update_rule(11, 17, {"Tuesday"})
    available_slots = invitee2.search_available_slots()
    for slot in available_slots:
        print(slot)

    # Invitees searching and booking slots
    print("\n--- Invitees Searching for Available Slots and Booking ---")

    # Example: Searching and booking operations
    available_slots = invitee1.search_available_slots()
    for slot in available_slots:
        print(slot)

    result = invitee1.book_slot("2024-12-09", "10 AM", "11 AM", "Monday")
    print(result)

        # Attempt to book the same slot (duplicate booking)
    print("\nInvitee3 (Charlie) attempts to book the same slot as Invitee1 (Alice) with Owner1 (John Doe):")
    # Charlie tries to book the same time slot already booked by Alice
    result = invitee3.book_slot("2024-12-09", "10 AM", "11 AM", "Monday")
    print(result)

    # Invitee2 (Bob) books a slot with Owner2 (Jane Smith)
    print("\nInvitee2 (Bob) booking a slot with Owner2 (Jane Smith):")
    # Bob successfully books a time slot with Jane Smith on a Tuesday
    result = invitee2.book_slot("2024-12-10", "9 AM", "10 AM", "Tuesday")
    print(result)

    # Invitee4 (Diana) books a slot with Owner2 (Jane Smith)
    print("\nInvitee4 (Diana) booking a slot with Owner2 (Jane Smith):")
    # Diana successfully books a time slot with Jane Smith on the same day as Bob, but at a different time
    result = invitee4.book_slot("2024-12-10", "10 AM", "11 AM", "Tuesday")
    print(result)

    # Invitee5 (Eve) searches available slots for Owner1 (John Doe)
    print("\nInvitee5 (Eve) searching available slots for Owner1 (John Doe):")
    # Eve searches for available time slots in John Doe's calendar
    available_slots = invitee5.search_available_slots()
    for slot in available_slots:
        print(slot)

    # Invitee5 (Eve) books a slot with Owner1 (John Doe)
    print("\nInvitee5 (Eve) booking a slot with Owner1 (John Doe):")
    # Eve books an available time slot with John Doe on a Friday
    result = invitee5.book_slot("2024-12-13", "2 PM", "3 PM", "Friday")
    print(result)

    # Show all booked slots for Owner1 (John Doe)
    print("\nAll booked slots for Owner1 (John Doe):")
    # Display all appointments booked in John Doe's calendar
    for appointment in owner1.list_appointments():
        print(appointment)

    # Show all booked slots for Owner2 (Jane Smith)
    print("\nAll booked slots for Owner2 (Jane Smith):")
    # Display all appointments booked in Jane Smith's calendar
    for appointment in owner2.list_appointments():
        print(appointment)


