# Event Manager

## Description

This application allows users to create, view, and delete events. Each event has a title, description, date, and time. Users can list all events and delete specific events by title. The application provides a simple text-based interface in the command line.

## Requirements

### Data Storage

Events are stored in a simple in-memory structure.

### Event Creation

- Function to add a new event with title, description, date, and time.
- Validation of date and time format (YYYY-MM-DD for date, HH:MM for time).

### Listing Events

- Function to display all events, sorted by date and time.
- Display all details of each event.

### Deleting Events

- Function to delete an event based on the title.
- Display appropriate message if the event does not exist.

### User Interface

- Simple text-based interface in the command line.

## Evaluation Criteria

- Code Quality: Readability, use of functions/classes, and adherence to Pythonic principles.
- Functionality: All features work as described.
- Error Handling: Gracefully handles invalid inputs and errors.
- Efficiency: Uses efficient algorithms and data structures where applicable.

## Submission

Submit the code as a GitHub repository link.

## Optional Advanced Features

- Implement a simple search functionality to find events by date or keyword in the title/description.
- Add the ability to edit existing events.
- Implement basic unit tests for the application.
