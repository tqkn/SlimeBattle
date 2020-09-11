import pygame
import sys
import char

#Importing keys from pygame.locals
from pygame.locals import (
    K_w,
    K_s,
    K_a,
    K_d,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#Initilize the pygame library 
pygame.init()

#Setting display size
SCREEN_X = 320
SCREEN_Y = 240
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))

player1 = char.Player()

running = True
while running:

    #Check if user closed game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #Filling background with white
    screen.fill((0, 0, 0))

    #Render in character
    # Draw the player on the screen
    screen.blit(player1.surf, (SCREEN_X/2, SCREEN_Y/2))

    #Update the display
    pygame.display.flip()

#Game quit 
pygame.quit()
