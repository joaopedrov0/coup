class Game:
    def __init__(self, playerList, Deck, options): # Lista de jogadores, baralho escolhido, objeto contendo customizações sobre o jogo
        self.playerList = playerList
        self.deck = Deck
        self.options = options

class Player:
    def __init__(self, name, Game, options={}):
        self.name = name
        self.playerDeck = []
        self.options = options
        self.coin = 0
        self.game = Game


class Deck:
    def __init__(self, name, id, cardList):
        self.name = name
        self.id = id
        self.cardList = cardList

class Card:
    def __init__(self, name, type, id, Deck):
        self.name = name
        self.type = type
        self.id = id
        self.deck = Deck

deckList = [
    "A Falha Ancestral",
    "Lia",
    "Epifania",
    "Avatar",
    "Ordem Paranormal"
]

cardClassList = [
    "captain",
    "countess",
    "assassin",
    "ambassador",
    "duke",
    "inquisitor",
    "custom"
]

# Estrutura de nomes das imagens: "<deckid>_<cardid>.png"


