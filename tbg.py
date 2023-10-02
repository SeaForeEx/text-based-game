import os  # Import the 'os' module for screen clearing.

# Define a dictionary called 'rooms' that represents different rooms in the game.
rooms = {
    'start': {
        'description': 'You are in a dark room.',
        'north': 'room1'
    },
    'room1': {
        'description': 'You are in room 1.',
        'east': 'room2',
        'south': 'start'
    },
    'room2': {
        'description': 'You are in room 2.',
        'west': 'room1',
        'south': 'room3'
    },
    'room3': {
        'description': 'You are in room 3. You found the treasure! Congratulations!',
        'end': True
    }
}

# Define a function called 'show_room' that displays the description of the current room and available exits.
def show_room(room):
    print(room['description'])  # Print the room's description.

    # Check and print the available exits in the current room.
    if 'north' in room:
        print('There is a door to your north.')
    if 'east' in room:
        print('There is a door to your east.')
    if 'south' in room:
        print('There is a door to your south.')
    if 'west' in room:
        print('There is a door to your west.')

# Define a function called 'get_action' that gets the player's input and validates their chosen action.
def get_action(room):
    while True:
        action = input('What do you want to do? ').lower().strip()  # Get the player's input.

        # Check if the input corresponds to a valid exit in the current room.
        if action == 'north' and 'north' in room:
            return room['north']
        elif action == 'east' and 'east' in room:
            return room['east']
        elif action == 'south' and 'south' in room:
            return room['south']
        elif action == 'west' and 'west' in room:
            return room['west']
        else:
            print('Invalid action. Try again.')  # Print an error message for invalid actions.

# Initialize the game by setting the 'current_room' to the 'start' room.
current_room = rooms['start']

def clear_screen():
    # Clear the terminal screen based on the OS (for Windows and Unix-like systems).
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

# Continue the game loop until the 'end' key is found in the current room (indicating the end of the game).
while 'end' not in current_room:
    clear_screen()  # Clear the terminal screen.
    show_room(current_room)  # Display the current room's description and available exits.
    next_room = get_action(current_room)  # Get the next room based on the player's input.
    current_room = rooms[next_room]  # Update the 'current_room' to the next room.

# Print the final description of the room when the game ends.
print(current_room['description'])
