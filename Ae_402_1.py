import pygame
pink = (255, 153, 204)
black = (0,0,0)
size = (500,500)
pygame.init()
screen=pygame.display.set_mode(size)
pygame.display.set_caption("try_color")
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(pink)
    pygame.draw.line(screen,black,(250,0),(250,500),5)
    pygame.draw.line(screen,black,(0,250),(500,250),5)
    pygame.draw.circle(screen,black,(20,20),3,3)
    pygame.draw.ellipse(screen,black,[250,250,30,50],0)
    pygame.display.flip() 
    clock.tick(60)
pygame.quit()      