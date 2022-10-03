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
playerX_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y))# blit == drow



#Game Loop
running = True;
while running:
    # RGB = Red,Green,Blue;
    screen.fill((30, 0, 0))#screen clor

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check wether its right ot left
        if event.type  == pygame.KEYDOWN:
            print("A keystoke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change =-0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
                print("Right arrow is pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame .K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change=0
                print("KeyStoke has been released")

    #5 = 5 + -0.1=5
    playerX += playerX_change
    player(playerX,playerY)
    pygame.display.update()







