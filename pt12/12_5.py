class Ship():
    battle_station = []
    def __init__(self, name: str, location: list):
        self.name = name
        self.locations = location
        self.damage = []
      
        for location in self.locations:
          Ship.battle_station.append(location)

    def has_overlap(self) -> bool:
        return len(set(Ship.battle_station)) != len(Ship.battle_station)

    def get_name(self) -> str:
        return self.name[0].upper()

    def get_full_name(self) -> str:
        return self.name
    
    def get_locations(self) -> list:
        return self.locations
  
    def take_damage(self, location) -> None:
        self.damage.append(location)

    def has_full_damage(self) -> bool:
        return len(self.damage) == len(self.locations)


def read_file() -> bool:
    file = input('Enter file name: ')
    # if len(file) == 0: file = 'board.txt'

    try:
        file_handle = open(file,'r')
        global SHIP_LIST
        
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
            SHIP_LIST.append( Ship_object )
            
            if Ship_object.has_overlap():
                print('There are overlapping ships in the input file!')
                return False
        
        return True
            
    except:
        print('File cannot be read!')
        return False

        
def get_valid_coordinate(xy_coord: str) -> tuple or None:
    global ALPHABET
    try:
        assert len(xy_coord) == 2
        (x_coord_txt, y_coord_txt) = [coord for coord in xy_coord]
        x_coord = ALPHABET.index(x_coord_txt.upper())
        y_coord = int(y_coord_txt)
        assert 0 <= y_coord <= 9
        return (x_coord, y_coord)
    except:
        return None

        
def print_board(current_board: list) -> None:
    global ALPHABET, BOARD_SIDE

    print()
    print(' '*2 + ' '.join(ALPHABET) + ' '*2)
    for row_index in range(BOARD_SIDE):
        row_content: list = current_board[row_index]
        row_number_txt: str = str(row_index)
        
        print(row_number_txt + ' ' + ' '.join(row_content)  + ' ' + row_number_txt)

    print(' '*2 + ' '.join(ALPHABET) + ' '*2)
    print()


def shoot_coordiate(current_board: list, x_coord: int, y_coord: int) -> list:
    update_board: list = current_board[:]
    marking: str = '*'
    global SHIP_LIST

    xy_coord: str = ALPHABET[x_coord] + str(y_coord);
    
    for ship in SHIP_LIST:
        ship_locations: list = ship.get_locations()
        if xy_coord in ship_locations:
            marking = 'X'
            ship.take_damage(xy_coord);
            if ship.has_full_damage():
                sunk_ship = ship
                marking = ship.get_name()
                print(f'You sunk a {ship.get_full_name()}!')

    if marking == '*' or marking == 'X':
        update_board[y_coord][x_coord] = marking
    else:
        update_board = reveal_ship(update_board, sunk_ship)
        
    return update_board


def reveal_ship(current_board: list, sunk_ship: Ship) -> list:
    update_board: list = current_board[:]
    ship_name: str = sunk_ship.get_name()
    ship_locations: list = sunk_ship.get_locations()
    global ALPHABET
    
    for location in ship_locations:
        (x_coord, y_coord) = get_valid_coordinate(location)
        update_board[y_coord][x_coord] = ship_name
  
    return update_board


def has_sunk_all_ship() -> bool:
    global SHIP_LIST
    ship_count = len(SHIP_LIST)
    sunk_ship_count = sum([1 for ship in SHIP_LIST if ship.has_full_damage()])
    
    return sunk_ship_count == ship_count

ALPHABET: list = ['A','B','C','D','E','F','G','H','I','J']
BOARD_SIDE: int = 10
SHIP_LIST: list = []

def main():

    board = [[' ']*10 for _ in range(10)]
    shot_location = []

    read_file_exit_status = read_file()
    if not read_file_exit_status:
        return False
    
    while True:
        print_board(board)

        if has_sunk_all_ship():
            print('Congratulations! You sank all enemy ships.')
            break
            
        user_input = input('Enter place to shoot (q to quit): ')
       
        if user_input.upper() == 'Q':
            print('Aborting game!')
            break  

        try:
            (x_coord, y_coord) = get_valid_coordinate(user_input)
        except:
            print('Invalid command!')
            continue

        if user_input in shot_location:
            print('Location has already been shot at!')
            continue
        
        board = shoot_coordiate(board, x_coord, y_coord)
        shot_location.append(user_input)

    return True

if __name__ == "__main__":
    main()

