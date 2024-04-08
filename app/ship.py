from app.deck import Deck


class Ship:
    def __init__(self, start, end, is_drowned=False):
        self.decks = self.create_decks(start, end)
        self.is_drowned = is_drowned

    @staticmethod
    def create_decks(start, end):
        decks = []
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                decks.append(Deck(i, j))
        return decks

    def get_deck(self, row, column):
        for deck in self.decks:
            if deck.row == row and deck.column == column:
                return deck
        return None

    def fire(self, row, column):
        deck = self.get_deck(row, column)
        if deck:
            deck.is_alive = False
            self.check_if_drowned()
            return True
        return False

    def check_if_drowned(self):
        alive_decks = [deck for deck in self.decks if deck.is_alive]
        if len(alive_decks) == 0:
            self.is_drowned = True
