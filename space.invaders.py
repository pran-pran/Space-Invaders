import pygame
from pygame import mixer

import math
import random 

# initialise pygame
pygame.init()

# create screen
screen = pygame.display.set_mode( (800,600) )

# background
background = pygame.image.load('background.png')

# background sound 
mixer.music.load('bgmusic.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = [] 
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10

# ready = can't see bullet, fire = bullet moving
bullet_state = "ready"

# score font
score_value = 0
font = pygame.font.Font('fungames.ttf', 32)
textX = 10
textY = 10

# game over font
over_font = pygame.font.Font('fungames.ttf', 64) 

# start screen font
start_font = pygame.font.Font('fungames.ttf', 55)

def show_score(x,y):
    score = font.render("score: " + str(score_value), True, (252,123,84))
    screen.blit(score, (x , y))

def game_over_text():
    over_text = over_font.render("game over :(", True, (255,255,255))
    screen.blit(over_text, (200, 250))

def start_game_text():
    start_text = start_font.render("Press SPACE to Start", True, (255, 255, 255))
    screen.blit(start_text, (80, 250))

def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x, y))   

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10)) 

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt( (math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)) )
    if distance < 30:
        return True
    else:
        return False  
    
def show_start_screen():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        start_game_text()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False


level = 1

# level-up sound
level_up_sound = mixer.Sound('levelsnd.mp3')


def show_level(x, y):
    level_text = font.render("Level: " + str(level), True, (252, 123, 84))
    screen.blit(level_text, (x, y))

def update_level():
    global level
    if score_value > 0 and score_value % 10 == 0:
        new_level = score_value // 10 + 1
        if new_level != level:
            level = new_level
            for i in range(num_of_enemies):
                enemyX_change[i] = 4 + (level - 1) * 2
                level_up_sound.set_volume(1.0)
                level_up_sound.play() 

# game running loop
def game_loop():
    global playerX, playerX_change, bulletX, bulletY, bullet_state, score_value


    running = True
    while running:
    
        # rgb
        screen.fill((0,0,0))

        # background img
        screen.blit(background, (0,0))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if keystroke pressed, check left or right
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound('laser.wav')
                        bullet_sound.set_volume(0.7)
                        bullet_sound.play() 
                        # get current x cord of spaceship
                        bulletX = playerX 
                        fire_bullet(bulletX, bulletY)
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

    # checking for boundaries
        playerX += playerX_change

        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        update_level()

    # enemy movement
        for i in range(num_of_enemies):  

            # game over
            if enemyY[i] > 400:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 4
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -4
                enemyY[i] += enemyY_change[i]
    
        # collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                collision_sound = mixer.Sound('explosion.wav')
                collision_sound.set_volume(0.7)
                collision_sound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 735)
                enemyY[i] = random.randint(50, 150)
        
            enemy(enemyX[i], enemyY[i], i)

    # bullet movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"
        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change


        player(playerX, playerY) 
        show_score(textX, textY)
        show_level(650, textY)
        pygame.display.update()

show_start_screen()
game_loop()