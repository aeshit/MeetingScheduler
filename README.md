# MeetingScheduler
Python implementation of MeetingScheduler

## Overview

This system allows `CalendarOwner`s to define their availability and enables `Invitee`s to search for and book available slots in their calendar. The data is managed in an in-memory singleton database. The system provides APIs for managing calendars, adding appointments, and searching for available time slots.

---

## How to Run

### Option 1: Executable File
1. Download the executable file.
2. Simply run the executable file, which should work directly without requiring any additional setup.
3. The application will load, and you can interact with the system as intended.

### Option 2: Run in IDE
1. Fork the repository to your local machine.
2. Install any required dependencies using `pip install -r requirements.txt`.
3. Open the project in your preferred IDE (e.g., PyCharm, VSCode).
4. Run the `main.py` to start the system.
5. The application will start, and you can interact with the APIs or use the provided functionality.

---

## Assumptions

1. An `Invitee` is mapped to one `CalendarOwner`. This can be extended to support multiple owners if needed by introducing an additional object to represent the relationship between multiple owners and invitees.
2. The system assumes that `Appointment` slots are strictly 1 hour long. Any other durations would need to be handled by extending the current logic.
3. The in-memory database is used for data storage, and it will be cleared once the system is restarted.

---

## Available APIs

### Calendar Owner Management

1. **add_calendar_owner(calendar_owner_id: str, calendar_owner: CalendarOwner)**:
   - Adds a new `CalendarOwner` to the in-memory database.
   - **Parameters**:
     - `calendar_owner_id`: Unique identifier for the `CalendarOwner`.
     - `calendar_owner`: Instance of `CalendarOwner` to be added.
   - **Returns**: None.

2. **get_calendar_owner(calendar_owner_id: str) -> CalendarOwner**:
   - Retrieves a `CalendarOwner` by their unique identifier.
   - **Parameters**:
     - `calendar_owner_id`: Unique identifier for the `CalendarOwner`.
   - **Returns**: Instance of `CalendarOwner` or `None` if not found.

3. **list_calendar_owners() -> List[CalendarOwner]**:
   - Lists all `CalendarOwner`s in the system.
   - **Returns**: List of `CalendarOwner` instances.

4. **log_data()**:
   - Debugging function that prints the stored `CalendarOwner` data.
   - **Returns**: None.

---

### Appointment Management

5. **add_appointment(calendar_owner_id: str, appointment: Appointment)**:
   - Adds an appointment to a `CalendarOwner`'s calendar.
   - **Parameters**:
     - `calendar_owner_id`: Unique identifier of the `CalendarOwner` who owns the calendar.
     - `appointment`: Instance of `Appointment` to be added.
   - **Returns**: Confirmation message indicating success.

6. **list_upcoming_appointments(calendar_owner_id: str) -> List[Appointment]**:
   - Retrieves a list of upcoming appointments for a specific `CalendarOwner`.
   - **Parameters**:
     - `calendar_owner_id`: Unique identifier for the `CalendarOwner`.
   - **Returns**: List of `Appointment` instances.

---

### Availability Rule Management

7. **set_availability_rule(calendar_owner_id: str, availability_rule: AvailabilityRule)**:
   - Sets or updates the availability rules for a specific `CalendarOwner`.
   - **Parameters**:
     - `calendar_owner_id`: Unique identifier for the `CalendarOwner`.
     - `availability_rule`: Instance of `AvailabilityRule` to be set.
   - **Returns**: None.

8. **get_availability_rule(calendar_owner_id: str) -> AvailabilityRule**:
   - Retrieves the availability rules for a specific `CalendarOwner`.
   - **Parameters**:
     - `calendar_owner_id`: Unique identifier for the `CalendarOwner`.
   - **Returns**: Instance of `AvailabilityRule`.

---

### Invitee Management

9. **search_available_slots(calendar_owner_id: str) -> List[str]**:
   - Searches for available time slots in a `CalendarOwner`'s calendar.
   - **Parameters**:
     - `calendar_owner_id`: Unique identifier for the `CalendarOwner`.
   - **Returns**: List of available time slots (formatted as `YYYY-MM-DD Day Time: StartHour:00 - EndHour:00`).

10. **book_slot(calendar_owner_id: str, date: str, start_time: str, end_time: str, invitee_name: str) -> str**:
    - Books an available time slot for an `Invitee` in the `CalendarOwner`'s calendar.
    - **Parameters**:
      - `calendar_owner_id`: Unique identifier for the `CalendarOwner`.
      - `date`: Date of the appointment (formatted as `YYYY-MM-DD`).
      - `start_time`: Start time of the appointment (formatted as `HH:MM`).
      - `end_time`: End time of the appointment (formatted as `HH:MM`).
      - `invitee_name`: Name of the invitee booking the slot.
    - **Returns**: Confirmation message indicating whether the booking was successful or not.

---

### In-Memory Database Management

11. **get_instance() -> InMemoryDatabase**:
    - Retrieves the singleton instance of the in-memory database.
    - **Returns**: Singleton instance of `InMemoryDatabase`.

12. **get_all_data() -> Dict**:
    - Retrieves all data stored in the in-memory database.
    - **Returns**: Dictionary containing all stored data, including `CalendarOwner` and `Appointment` information.

---

## Example Workflow

1. **Add a Calendar Owner**:
   - I can create and add a new `CalendarOwner` to the system using `add_calendar_owner()`.

2. **Set Availability Rules**:
   - I can set the availability for a `CalendarOwner` using `set_availability_rule()`.

3. **Search Available Slots**:
   - As an `Invitee`, I can search for available slots in a `CalendarOwner`'s calendar using `search_available_slots()`.

4. **Book an Appointment**:
   - I can book an available time slot using `book_slot()`.

5. **Add Appointments**:
   - The `CalendarOwner` can add appointments using `add_appointment()`.

6. **View Upcoming Appointments**:
   - I can view upcoming appointments using `list_upcoming_appointments()`.

---

## Challenges

### 1. Managing Overlapping Appointments with High Accuracy
When booking appointments, ensuring that no time slots overlap was a technical challenge, especially when working with a large number of appointments. Initially, the system didn't efficiently check for overlapping appointments, which sometimes resulted in double bookings. I addressed this issue by introducing a more sophisticated data structure (like a balanced tree or interval tree) to check for overlaps, ensuring that the system could handle appointments without overlap efficiently.

### 2. Executable File Generation Challenges
While using `pyinstaller` to package the system into an executable, I encountered significant performance issues. The executable file took too long to build due to the inclusion of a virtual environment (`venv`). The `venv` had a large number of dependencies, which caused the packaging process to slow down considerably. This challenge was mitigated by optimizing the virtual environment setup, carefully selecting only the necessary dependencies, and making sure the environment was as lean as possible. Additionally, using the `--onefile` flag with `pyinstaller` helped reduce the executable file size but still resulted in slower build times, which was an important consideration for future improvements.

---

## Conclusion

This system allows seamless management of appointments between `CalendarOwner` and `Invitee`, with APIs to manage availability, search for slots, and book appointments. The in-memory database provides a simple yet effective way to manage and store all the data. While I faced several technical challenges during the development, I was able to optimize performance and address edge cases, making the system both scalable and reliable.
