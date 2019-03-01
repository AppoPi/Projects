# 1 - Import library
import pygame
from pygame.locals import *
import pygame.gfxdraw

from matplotlib import path
import numpy as np
 
# 2 - Initialize the game
pygame.init()
width, height = 500, 500
screen = pygame.display.set_mode((width, height))

# from PIL import Image, ImageDraw

# im = Image.new('RGB', (width, height))
# draw = ImageDraw.Draw(im)

# for i in range(50, width-50, 50):
    # for j in range(50, height-50, 50):
        # coor = (i, j, i+50, j+50)
        # draw.rectangle(coor, outline='black', fill='white')

# im.save('image.png')

# im = pygame.image.load('image.png')

white = (255,255,255)
black = (0, 0, 0)
yellow = (100, 100, 0)
clock = pygame.time.Clock()
quit = False

font = pygame.font.SysFont("monospace", 15)


while not quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
    screen.fill(white)
    
    # screen.blit(im, (0,0))
    x1 = 50
    y1 = 300
    w = 50
    h = 50
    
    mousex, mousey = pygame.mouse.get_pos()
    mousecoor = (mousex, mousey)
    # coor1 = [(x1 + w, y1 - h),(x1 + 2 * w, y1 - h), (x1 + w, y1), (x1,y1)]
    coor1 = [(x1, y1), (x1 + w, y1), (x1 + w, y1 + h), (x1, y1 + h)]
    p1 = path.Path(coor1)
    
    label = font.render(str(mousecoor), 1, (255,0,0))
    screen.blit(label, (50, 30))
    
    if p1.contains_point((mousex, mousey)):
        # pygame.draw.polygon(screen, yellow, [(50,300), (250,400), (450,300),(250, 200)], 2)
        pygame.gfxdraw.filled_polygon(screen, coor1, yellow)
    else:
        # pygame.draw.polygon(screen, black, [(50,300), (250,400), (450,300),(250, 200)], 2)
        pygame.gfxdraw.filled_polygon(screen, coor1, black)
    
    
    pygame.display.flip()
    clock.tick(60)
