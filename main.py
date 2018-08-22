import pygame
#from PIL import Image
from playerClass import Player
#import playerClass
#import WallClass
from WallClass import Wall
from numpy import loadtxt
#import numpy
#from PlusClass import Plus
#from NodeClass import Node
from GhostClass import Ghost
#import GhostClass
#import networkx as nx
#import collections
pygame.init()


#################################################
####################### VARIABLES ###############
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,128,248)
green  =(0,255,0)

displayWidth = 550
displayHeight = 530
width , height = (20,15)


gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("PacMan")

FBS =12
size = 14

clock = pygame.time.Clock()

font = pygame.font.SysFont(None,25)
    
gameOver = False
changeDirectionPositions = []
all_sprites = pygame.sprite.Group()

walls = pygame.sprite.Group()
pluses = pygame.sprite.Group()
ghosts = pygame.sprite.Group()



layout = loadtxt('a.txt', dtype=str)
rows, cols = layout.shape
for col in range(cols):
    for row in range(rows):
        value = layout[row][col]
        lead_x = col*width
        lead_y = row*height
        if value == '0':
            pos = (col*width, row*height)
            wall = Wall(blue,lead_x,lead_y)
            all_sprites.add(wall)
            walls.add(wall)


ghost = Ghost(12,white)
ghosts.add(ghost)
player = Player(size,ghosts)
all_sprites.add(player)
all_sprites.add(ghost)


###################################################
timer = 0;
while not gameOver:
    timer = timer +1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver= True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.direction = 1 
            elif event.key == pygame.K_DOWN:
                player.direction = 2
            elif event.key == pygame.K_LEFT:
                player.direction = 4
            elif event.key == pygame.K_RIGHT:
                player.direction = 3
                
            player.isCol = False
            
    playerPosition = (player.rect.x,player.rect.y)          
    all_sprites.update(walls,changeDirectionPositions)
    if timer % 2 == 0:
        for sprite in all_sprites:
            if sprite == ghost:
                sprite.movement(player.rect.x,player.rect.y)
    ## check for wall hits     
    gameDisplay.fill(black)
    all_sprites.draw(gameDisplay)

    pygame.display.update()
#    gameDisplay.blit(bg, [0, 0])
#    pygame.display.update()
       
    clock.tick(FBS)



pygame.quit()
    
            
    
