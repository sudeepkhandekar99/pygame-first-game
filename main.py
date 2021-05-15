import pygame

# Intialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("space boi")
icon = pygame.image.load('icon.img')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spirit.png')
playerX = 370
playerY = 480

def player(x, y):
    screen.blit(playerImg, (x, y))

# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Movements
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            print("Lpressed")
        if event.key == pygame.K_RIGHT:
            print("Rpressed")
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #print("Dpressed")
    
    player(playerX, playerY)
    pygame.display.update()