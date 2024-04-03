import datetime

# In-memory storage for events
events = []

# Function to add a new event
def add_event(title, description, date, time):
    # Validate date and time format
    try:
        event_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        event_time = datetime.datetime.strptime(time, '%H:%M').time()
    except ValueError:
        print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")
        return
    
    # Create a new event dictionary
    new_event = {
        'title': title,
        'description': description,
        'date': event_date,
        'time': event_time
    }
    
    # Add the event to the list
    events.append(new_event)
    print("Event added successfully.")

# Function to display all events
def list_events():
    if not events:
        print("No events found.")
        return
    
    # Sort events by date and time
    sorted_events = sorted(events, key=lambda x: (x['date'], x['time']))
    
    # Display all events
    for event in sorted_events:
        print(f"Title: {event['title']}")
        print(f"Description: {event['description']}")
        print(f"Date: {event['date']}")
        print(f"Time: {event['time']}")
        print()

# Function to delete an event
def delete_event(title):
    global events
    # Filter events to find the event with the given title
    filtered_events = [event for event in events if event['title'] == title]
    
    if filtered_events:
        # Remove the first occurrence of the event with the given title
        events.remove(filtered_events[0])
        print(f"Event '{title}' deleted successfully.")
    else:
        print(f"No event found with title '{title}'.")

# Main function to run the application
def main():
    while True:
        print("\nWelcome to Event Scheduler!")
        print("1. Add Event")
        print("2. List Events")
        print("3. Delete Event")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter event title: ")
            description = input("Enter event description: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            time = input("Enter event time (HH:MM): ")
            add_event(title, description, date, time)
        elif choice == '2':
            list_events()
        elif choice == '3':
            title = input("Enter title of event to delete: ")
            delete_event(title)
        elif choice == '4':
            print("Thank you for using Event Scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
