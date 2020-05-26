import math, pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Polygon with sides > 3 is impossible in Euclidean Space
n = 3
r = 150


pygame.init()
pygame.font.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Polygon Area Calculator")

myfont = pygame.font.SysFont('Comic Sans MS', 16)
textsurface = myfont.render("", False, WHITE)

clock = pygame.time.Clock()
on = True

while on:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False
            pygame.quit()
 

        thetaR = 2*math.pi/n
        y = n/2 * r**2 * math.sin(thetaR)
        p = n * ( math.sin(thetaR)/math.sin( (2*math.pi-thetaR)/2 ) )

        info = f"Sides: {n} Area: {y} Theta (Degrees): {360/n}"    
        textsurface = myfont.render(info, False, WHITE)

        screen.fill(BLACK)

        screen.blit(textsurface,(0,0))

        pygame.draw.circle(screen, RED, (350,250), r, 1)

        points = []
        for i in range(n):
            x = r*math.sin(thetaR*i)+350
            y = r*math.cos(thetaR*i)+250
            points.append([x,y])

        pygame.draw.polygon(screen, WHITE, points, 1) 

        pygame.display.flip()

        n += 1
        clock.tick(1)

pygame.quit()
