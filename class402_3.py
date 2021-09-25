import pygame
pygame.init()
size = (500,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("mouse")
done = False
clock = pygame.time.Clock()
white = (255,255,255)
red = (255,0,0)
x=0
y=0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 1
        if x <=0:
            x=0
    elif keys[pygame.K_RIGHT]:
        x += 1
        if x >=490:
            x=490
    elif keys[pygame.K_UP]:
        y -= 1
        if y <= 0:
            y=0
    elif keys[pygame.K_DOWN]:
        y += 1
        if y >=490:
            y=490
    else:
        pass
    screen.fill(white)
    pygame.draw.rect(screen, red, [x , y , 10, 10])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
            
 
