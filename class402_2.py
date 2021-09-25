import pygame
import random
pygame.init()
size = (500,500)
def randColour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return(r,g,b)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("mouse")
done = False
clock = pygame.time.Clock()
click = False
limit = 30
count = 0
black = (0,0,0)
pos = (0,0)
color = randColour()
while not done:
    screen.fill(black)
    if click and count < limit:
        pygame.draw.circle(screen,color,pos,count)
        count +=1
    if count >= limit:
            click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            click = True
            count = 0
            color = randColour()
            print(pos)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
                                 

