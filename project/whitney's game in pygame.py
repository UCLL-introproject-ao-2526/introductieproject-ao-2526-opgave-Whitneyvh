import random
import pygame

# game variables / deck
# cards zijn 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
# cards classes/suits zijn Nature, Water, fire and wind


pygame.init()

#pygame window
WIDTH = 600
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('pygame Blackjack!')
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 44)
smaller_font = pygame.font.Font('freesansbold.ttf', 36)
active = False
# win, loss, draw/push/tie
# win, loss, draw/push/tie
records = [0, 0, 0]
player_score = 0
dealer_score = 0
initial_deal = False
my_hand = []
dealer_hand = []
outcome = 0
reveal_dealer = False
hand_active = False
outcome = 0
add_score = False
results = ['', 'Player WINS! :)', 'Computer WINS :(', 'TIE GAME...']



# building our deck
def build_deck():
    deck = []
    elements = ["natuur", "vuur", "wind", "water"]
    values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    for element in elements:
        for value in values:
            cardval = "{} {}".format(element, value)
            deck.append(cardval)
    return deck



# deal cards by selecting randomly from deck, and make function for one card at a time
def shuffle_deck(deck):
    for cardpos in range(len(deck)):
        randpos = random.randint(0,55)
        deck[cardpos], deck[randpos] = deck[randpos], deck[cardpos]
    return deck



# draw card function that draws a specified number of cards from the top of the deck
def draw_cards(num_cards):
    cards_drawn = []
    for x in range(num_cards):
        cards_drawn.append(whitney_deck.pop(0))
    return cards_drawn



# a function to show our hand
def show_hand(player, player_hand):
    print("player {}".format(player+1))
    print("your hand")
    print("----------------")
    for card in player_hand:
        print(card)
    print("")



whitney_deck = build_deck()
whitney_deck = shuffle_deck(whitney_deck)
discards = []
print(whitney_deck)

player1 = draw_cards(5)
player2 = draw_cards(5)


player_turn = 0
playing = True
discards.append(whitney_deck.pop(0))

while playing:
    show_hand(player_turn, player1[player_turn])
    print("card on top of discard pile: {}".format(discards[-1]))

