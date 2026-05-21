# black jack in python with pygame!
import copy # makes a copy, needed for example when you play a game it copies the deck. you play with the copied deck if you discard one there it does not change the original deck.
import random # makes it all unpredictable so to speak it makes randomness possible like reshuffeling the deck makes it different everytime.
import pygame # is the toolbox for making games.


# game variables
cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']
# these are strings not integers cause they also have letters. that is why they stand between '' 
# [this means that it is a list, in order, it means that cards does not have 1 value but this entire list of values]

one_deck = 4 * cards
# this means that we are multiplying the deck 4 times to make a full deck

decks = 4
# we are making 4 decks in this game because blackjack uses 4 different decks to prevent cardcounting
# this is the amount of decks the game needs

game_deck = copy.deepcopy(decks * one_deck)
# we make a copy so that the playing deck is a copy of the original one. if the playing one is shuffeld/discarted/... it does not change anything in the original one.
# we do not make any suits here because in blackjack it is not needed. every suit has the same worth and suits are useless in the game.

pygame.init()
# needed to put this in cause it kept giving a error in the code for the font. 
# This makes sure it initializes all the modules we want tu use like the font, the sound, the timers, etc.

#pygame window
WIDTH = 600
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
# this is to use the settings to have the display

pygame.display.set_caption('pygame Blackjack!')
# this is for the title, so that the game has a name in the gamingdisplay

fps = 60
# this is for the amount of frames per second, so that means the smoothness of the game.

timer = pygame.time.Clock()
# we need this to make the fps work, without this the game would run as fast as your computer can handle it. 
# With the clock it gives you an amount of time in where the fps is run.

font = pygame.font.Font('freesansbold.ttf', 44)
# this is the font we are going to use.

active = False


# draw game conditions and buttons
def draw_game(act): 
    # He makes a function here that is responsible for making a drawing in the game
    button_list = []
    # Initially on startip (not active) only option is to deal new hand
    if not act:
        deal = pygame.draw.rect(screen, 'white', [150, 20, 300, 100], 0, 5)
        pygame.draw.rect(screen, 'green', [150, 20, 300, 100], 3, 5)
        deal_text = font.render('DEAL HAND', True, 'black')
        screen.blit(deal_text, (165, 50))
        button_list.append(deal)





#main game loop
run = True
# this means that the game can keep on running over and over again, like a loop.
while run:
    # this means that as long as it is running: do everything all over agian.
    # So that means for this clean the screen, draw everything again, make the screen clean, ... 60 times per second
    # run game at our framerate and fill screen with bg color
    timer.tick(fps)
    #this means that the loop cannot go any faster than the appointed speed, otherwise the game would go turbospeed
    screen.fill('black')
    # This part makes the screen of the game black
    buttons = draw_game(active)
    #

    # event handling, if quit pressed, then exit game
    for event in pygame.event.get():
        # this means that it checks every event you or the system did since the previous frame.
        # without this your game wouldn't get any input, and you couldn't continu
        # Imagine this: if in the previous frame you clicked hit then you need to get a card. If your game does not know your previous input, it wouldn't give you a card.
        if event.type == pygame.QUIT:
            # This means that if you press quit - 
            run = False
            # - the loop ends

        pygame.display.flip()
        # This says that it has to show everthing that was drawn on the screen.
        # So fill means black screen in this case, flip means show it.
pygame.QUIT()
# This ends the loop