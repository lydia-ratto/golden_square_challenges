1. User Journey
    As a player
    So that I can prepare for the game
    I would like to place a ship in a board location

    As a player
    So that I can play a more interesting game
    I would like to have a range of ship sizes to choose from

    As a player
    So that I can win the game
    I would like to be able to fire at my opponent's board

    As a player
    So that I can refine my strategy
    I would like to know when I have sunk an opponent's ship

2. Design classes and methods
class Ship
    def __init__(self, type):
        Params:
            type, as string with options Carrier, Battleship, Destroyer, Submarine, Patrol Boat
        Returns:
        Side-effects:
            size, as number 5 if Carrier, 4 if Battleship, 3 if Destroyer or Submarine, 2 if Patrol Boat
            lives, set to size
            coordinates, as empty list

    def set_coordinate():
        Params:
            letter as string, in range A-J
            number as string, in range 1-10
        Returns:
        Side-effects:
            checks if coordinate already present in coordinates list
            checks if coordinate list has not exceeded 
            if not, creates coordinate
            else returns message 'Coordinate already taken'

    def hit:
        Params:

        Returns:
        Side-effects:
    
    def __init__():
        Params:
        Returns:
        Side-effects:

class ShipsOnBoard
    def __init__(self):
        Params:
        Returns:
        Side-effects:
            ships as empty list
    
    def add(self):
        Params:
            ship, as object
        Returns:
        Side-effects:
            check if Ship name count exceeds 1 for Carrier, 2 for Battleship, 3 for Destroyer, 4 for Submarine and 5 for Patrol
                if so, return message "Max number of X Ship exceeded"
            set ship position and verify if number of coordinates matches ship size of x number
                if number of coordinates is grater, return message 'You can only select x number of coordinates"
                if number of coordinates is smaller, return message 'You need to select x number of coordinates"
            
            check if position is available by comparing to other positions in list
                if available, add ship to list of ships
                else, return message "Positon taken"


class Coordinate:
    def __init__(self, letter, number, ship):
        Params:
            letter as string
            number as string
            ship as object
        Returns:
        Side-effects:
            sets letter
            sets number
            sets ship
            sets hit as boolean, default false

    def fire:
        

        
    