from src import *

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Predator-Prey")

clock = pygame.time.Clock()

# instanciar classes de agentes
# lista de agentes

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    SCREEN.fill(BLACK)
    
    #faz updates de agentes
    
    pygame.display.flip()
    clock.tick(FPS)