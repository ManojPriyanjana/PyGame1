import pygame

#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))
#Title and icon
pygame.display.set_caption("Space Catch -- Created By Manoj Priyanjana Dayasri")
icon = pygame.image.load("sources Manoj/icon/space-ship.png")
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("sources Manoj/GameImage/rocket.png")
playerX =370
playerY =480

def player():
    screen.blit(playerImg,(playerX,playerY))# blit == drow



#Game Loop
running = True;
while running:
    # RGB = Red,Green,Blue;
    screen.fill((30, 0, 0))#screen clor

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    player()
    pygame.display.update()







