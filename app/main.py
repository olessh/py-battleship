from app.ship import Ship


class Battleship:
    def __init__(self, ships):
        self.field = {}
        self.ships = ships
        for ship in ships:
            self.place_ship(ship)

    def place_ship(self, ship_coords):
        ship = Ship(ship_coords[0], ship_coords[1])
        for i in range(ship_coords[0][0], ship_coords[1][0] + 1):
            for j in range(ship_coords[0][1], ship_coords[1][1] + 1):
                self.field[(i, j)] = ship

    def fire(self, location: tuple):
        if location in self.field:
            ship = self.field[location]
            all_decks_sunk = all(not deck.is_alive for deck in ship.decks)
            if all_decks_sunk:
                return "Sunk!"
            else:
                return "Hit!"
        else:
            return "Miss!"

    # def print_field(self):
    #     for i in range(10):
    #         for j in range(10):
    #             location = (i, j)
    #             if location in self.field:
    #                 ship = self.field[location]
    #                 for deck in ship.decks:
    #                     if deck.row == location[0] and deck.column == location[1]:
    #                         if deck.is_alive:
    #                             print(u"\u25A1", end=" ")
    #                         else:
    #                             if ship.is_drowned:
    #                                 print("x", end=" ")
    #                             else:
    #                                 print("*", end=" ")
    #             else:
    #                 print("~", end=" ")
    #         print()
