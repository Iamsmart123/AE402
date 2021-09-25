import pygame,random
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
x=[300,250,200,250]
y=[250,250,250,200]
pygame.init()
done = False
size = (700,500)
screen= pygame.display.set_mode(size)
pygame.display.set_caption("game")
clock=pygame.time.Clock()
def new_color(choice):
    tmp=random.randint(0,3)
    while choice == tmp:
        tmp=random.randint(0,3)
    choice = tmp
    return choice
choice = random.randint(0,3)
score = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            if(choice == 2):
                choice =new_color(choice)
                score = score+1
        elif event.key == pygame.K_RIGHT:
            if(choice == 0):
                choice =new_color(choice)
                score = score+1
        elif event.key == pygame.K_UP:
            if(choice == 3):
                choice =new_color(choice)
                score = score+1
        elif event.key == pygame.K_DOWN:
            if(choice == 1):
                choice =new_color(choice)
                score = score+1
    for i in range(4):
        if i == choice:
            color = YELLOW
        else:
            color = BLACK
        pygame.draw.rect(screen,color,[x[i],y[i],40,40])
    pygame.display.set_caption(str(score)) 
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

           

