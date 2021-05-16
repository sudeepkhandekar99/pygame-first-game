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
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('alien.png')
enemyX = 370
enemyY = 50
enemyX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game Loop
running = True
while running:
    screen.fill((150, 150, 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movements
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > 768:
        playerX = 768
        
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
