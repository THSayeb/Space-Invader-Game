import pygame
import math
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 500
PLAYER_START_X, PLAYER_START_Y = 370, 380
ENEMY_START_Y_MIN, ENEMY_START_Y_MAX = 50, 150
ENEMY_SPEED_X, ENEMY_SPEED_Y = 4, 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Invader')

#icon
icon = pygame.image.load('IconImage.jpeg')
pygame.display.set_icon(icon)

#player image
playerImg = pygame.image.load('PlayerImage.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

#Enemy
enemy_Img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_Img.append(pygame.image.load('EnemyImage.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH-64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX ))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

#bullet
bulletImg = pygame.image.load('BulletImage.jpeg')
bulletX , bulletY = 0, PLAYER_START_Y
bulletX_change, bulletY_change = 0, BULLET_SPEED_Y
bullet_state = 'ready '