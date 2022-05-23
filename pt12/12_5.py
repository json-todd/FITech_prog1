"""
COMP.CS.100
Chapter 12 Section 5: Battleship
Game description: On a 10x10 game board, the player attempts to sink the computer's fleet.
Player declare coordinates designating the tiles on gamebard, make educated guess, and deduce tiles containing enemy's ships.
Player won when all ships are sunk.

Author: Tri Phung
Email: tri.phung@tuni.fi
Student ID: tuni.fi:K441912

"""

class Ship():
    __battle_station = []
    def __init__(self, name: str, location: list):
        self.__name = name
        self.__locations = location
        self.__damage = []
      
        for location in self.__locations:
          Ship.__battle_station.append(location)

    def has_overlap(self) -> bool:
        """Return true if Ships have overlapping coordinates"""
        return len(set(Ship.__battle_station)) != len(Ship.__battle_station)

    def get_name(self) -> str:
        """Return capitalized initial letter of ship name"""
        return self.__name[0].upper()

    def get_full_name(self) -> str:
        """Return ship name"""
        return self.__name
    
    def get_locations(self) -> list:
        """Return all ship's locations"""
        return self.__locations
  
    def take_damage(self, location) -> None:
        """Register the location where the shit gets hit
        Hit location is then stored into an array for later implementation
        """
        self.__damage.append(location)

    def has_full_damage(self) -> bool:
        """When ship has all of its location hits, it has taken full damaged.
        Return true when ship is full damaged.
        """
        return len(self.__damage) == len(self.__locations)


class Board():
    ALPHABET: list = ['A','B','C','D','E','F','G','H','I','J']
    BOARD_SIDE: int = 10
    SHIP_LIST: list = []
    
    def __init__(self):
        pass
        
    @classmethod
    def add_ship(self, ship: Ship) -> None:
        """Add Ship to a class attribute"""
        Board.SHIP_LIST.append(ship)
    
    @classmethod
    def get_ships(self) -> list:
        """Return all ships on the board"""
        return Board.SHIP_LIST
    

def read_file() -> bool:
    """Read the input file

    Returns:
        bool: exit status of this function. True if success, False if error or invalid.
    """
    file = input('Enter file name: ')
    if len(file) == 0: file = 'board.txt'

    try:
        file_handle = open(file,'r')
        
        for line in file_handle:
            line = line.rstrip()
            data = line.split(';')
            name: str = data[0]
            coordinate: list = data[1:]
            
            for loc in coordinate:
                if get_valid_coordinate(loc) == None:  
                    print('Error in ship coordinates!')
                    return False
            
            
            Ship_object = Ship(name, coordinate)
            Board.add_ship( Ship_object )
            
            if Ship_object.has_overlap():
                print('There are overlapping ships in the input file!')
                return False
        
        return True
            
    except:
        print('File can not be read!')
        return False

        
def get_valid_coordinate(xy_coord: str) -> tuple or None:
    """Check and return the correct format of coordinate.

    Args:
        xy_coord (str): coordinate in format of ALPHABET-NUMBER, e.g. 'A1'

    Returns:
        tuple or None: coordinate of x and y in numerical type when valid. None otherwise
    """
    ALPHABET = Board.ALPHABET
    try:
        assert len(xy_coord) == 2
        (x_coord_txt, y_coord_txt) = [coord for coord in xy_coord]
        x_coord = ALPHABET.index(x_coord_txt.upper())
        y_coord = int(y_coord_txt)
        return (x_coord, y_coord)
    except:
        return None

        
def print_board(current_board: list) -> None:
    """Print the board with style

    Args:
        current_board (list): Game board
    """
    ALPHABET = Board.ALPHABET
    BOARD_SIDE = Board.BOARD_SIDE

    print()
    print(' '*2 + ' '.join(ALPHABET) + ' '*2)
    for row_index in range(BOARD_SIDE):
        row_content: list = current_board[row_index]
        row_number_txt: str = str(row_index)
        
        print(row_number_txt + ' ' + ' '.join(row_content)  + ' ' + row_number_txt)

    print(' '*2 + ' '.join(ALPHABET) + ' '*2)
    print()


def shoot_coordiate(current_board: list, x_coord: int, y_coord: int) -> list:
    """Shoot the location at `x_coord` and `y_coord`.
    Mark the tile appropriately.

    Args:
        current_board (list): game board
        x_coord (int): x coordinate, as an index for list accessing
        y_coord (int): y coordinate, as an index for list accessing

    Returns:
        update_board(list): mark at the shot locoation and update the board.
    """
    update_board: list = current_board[:]
    marking: str = '*'
    ship_list = Board.get_ships()
    ALPHABET = Board.ALPHABET
    xy_coord: str = ALPHABET[x_coord] + str(y_coord);
    
    for ship in ship_list:
        ship: Ship
        ship_locations: list = ship.get_locations()
        if xy_coord in ship_locations:
            marking = 'X'
            ship.take_damage(xy_coord);
            if ship.has_full_damage():
                sunk_ship = ship
                marking = ship.get_name()
                print(f'You sank a {ship.get_full_name()}!')

    if marking == '*' or marking == 'X':
        update_board[y_coord][x_coord] = marking
    else:
        update_board = reveal_ship(update_board, sunk_ship)
        
    return update_board


def reveal_ship(current_board: list, sunk_ship: Ship) -> list:
    """Reveal ship name at all occupying tiles when it has full damage.
    Tiles of ship location display ship's capitalized initial letter.

    Args:
        current_board (list): game board
        sunk_ship (Ship): ship object that has taken all of locations shot

    Returns:
        update_board(list): update game board where tiles reveal ship's capitalized initial letter.
    """
    update_board: list = current_board[:]
    ship_name: str = sunk_ship.get_name()
    ship_locations: list = sunk_ship.get_locations()
    
    for location in ship_locations:
        (x_coord, y_coord) = get_valid_coordinate(location)
        update_board[y_coord][x_coord] = ship_name
  
    return update_board


def has_sunk_all_ship() -> bool:
    """Return true if the number of ship sunk equals to the number of all ships"""
    ship_list = Board.get_ships()
    ship_count = len(ship_list)
    sunk_ship_count = sum([1 for ship in ship_list if ship.has_full_damage()])
    
    return sunk_ship_count == ship_count


def main():
    board = [[' ']*10 for _ in range(10)]
    shot_location = []

    # Read input file. If unsuccessful, program terminated
    read_file_exit_status = read_file()
    if not read_file_exit_status:
        return False
    
    # Main program loop
    while True:
        print_board(board)

        # Check winning condition. If true, loop ends
        if has_sunk_all_ship():
            print('Congratulations! You sank all enemy ships.')
            break
            
        user_input = input('Enter place to shoot (q to quit): ')
       
        if user_input.upper() == 'Q':
            print('Aborting game!')
            break  

        # Validate user's input to have right formate
        try:
            (x_coord, y_coord) = get_valid_coordinate(user_input)
        except:
            print('Invalid command!')
            continue

        # Validate location to be a new one
        if user_input.upper() in shot_location:
            print('Location has already been shot at!')
            continue
        
        # Proceed shooting at the coordinate
        # Add the shot coordinate in a historical ledger.
        board = shoot_coordiate(board, x_coord, y_coord)
        shot_location.append(user_input.upper())

    return True

if __name__ == "__main__":
    main()

