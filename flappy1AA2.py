import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=400
height=600
screen = pygame.display.set_mode((width,height))
  
#load the images in dict
images={}
images["bg1"] = pygame.image.load("bg1.png").convert_alpha()
images["base"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("redbird-midflap.png").convert_alpha()
images["pipe"] = pygame.image.load("pipe-red.png").convert_alpha()
images["message"] = pygame.image.load("message.png").convert_alpha()
images["over"] = pygame.image.load("gameover.png").convert_alpha()
images["cloud"]=pygame.image.load("cloud.png").convert_alpha()
bird= pygame.Rect(100,250,30,30)
groundx=0
x1=100    
while True:    
    screen.fill((50,150,255))
    screen.blit(images["bg1"],[0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
    
    groundx =groundx-5
    
    if groundx< -330:
        groundx=0
    
    x1=x1-5
    if x1< -200:
        x1=500
    
    
    screen.blit(images["cloud"],[x1,70])
    screen.blit(images["bird"],bird)    
    screen.blit(images["base"],[groundx,550])
   
    pygame.display.update()
    clock.tick(30)
    
    
    
    

