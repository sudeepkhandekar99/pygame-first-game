import math 
import random
import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.jpg')

# Background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemy_count = 20
for i in range(enemy_count):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(70, 700))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.15*2)
    enemyY_change.append(10*2)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"  # Bullet ready and fire states

# Game score 
score = 0
font = pygame.font.Font('freesansbold.ttf',20)
textX = 10
textY = 10 

# Game over
over_font = pygame.font.Font('freesansbold.ttf', 300)

def game_over_text():
    over_text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (350, 200))

def showScore(x, y):
    game_score = font.render("SCORE : " +  str(score), True, (255, 255, 255))
    screen.blit(game_score, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow((enemyX - bulletX), 2)+math.pow((enemyY - bulletY), 2))
    if distance < 27 :
            return True
    return False

# Game Loop
running = True
while running:
    # Background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movements
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_sound = mixer.Sound('bullet.wav')
                bullet_sound.play()
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            

    # Checking for boundaries
    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    for i in range(enemy_count):
        if enemyY[i] > 400:
            for j in range(enemy_count):
                enemyY[j] = 2000
            game_over_text()
            break
        
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.15
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.15
            enemyY[i] += enemyY_change[i]
            
        # Collison
        collison = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collison:
            explotion_sound = mixer.Sound('blast.wav')
            explotion_sound.play()
            bulletY = 480 
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(70, 700)
            enemyY[i] = random.randint(50, 150)
        
        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    showScore(textX, textY)
    pygame.display.update()
