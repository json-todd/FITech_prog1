class Ship():
    battle_station = []
    def __init__(self, name, *arg):
        self.name = name
        self.locations = list(arg)
        self.damage = []
      
        for location in self.locations:
          Ship.battle_station.append(location)

    def has_overlap(self) -> bool:
        return set(len(Ship.battle_station)) == len(Ship.battle_station)

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
