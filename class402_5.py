import pygame
red = (255,0,0)
Blue = (0,0,255)
Green = (0,255,0)
ORANGE = (242,133,0)
YELLOW = (255,255,0)
PURPLE = (255,0,255)
SKY = (135,206,255)

pygame.init()
done = False
size = (700,500)
screen= pygame.display.set_mode(size)
pygame.display.set_caption("Rainbow")
clock=pygame.time.Clock()
color = [red,Blue,Green,ORANGE,YELLOW,PURPLE]
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(SKY)
    for i in range(len(color)):
        pygame.draw.arc(screen,color[i],[100-i*10,200-i*10,300+i*20,300+i*20],0,3,10) 
    pygame.draw.circle(screen,YELLOW,[500,100],60)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()