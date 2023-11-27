from src import *

#pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Predator-Prey")

clock = pygame.time.Clock()

# lista de agentes
preys = [Prey() for i in range(10)]
predators = [Predator() for i in range(10)]
plants = [Plant() for i in range(100)]

def handlePlants():
    global plants
    plants = [p for p in plants if p.is_alive is True]
    plants = plants + [Plant() for _ in range(2)]
    
def handlePreys():
    global preys
    preys = [p for p in preys if p.is_alive is True]
    
    for p in preys[:]:
        if p.energy > 5:
            p.energy = 0
            preys.append(Prey(x = p.x + random.randint(-20, 20), y = p.y + random.randint(-20, 20)))

def handlePredators():
    global predators
    predators = [p for p in predators if p.age < 2000]
    
    for p in predators[:]:
        if p.energy > 10:
            p.energy = 0
            predators.append(Predator(x = p.x + random.randint(-20, 20), y = p.y + random.randint(-20, 20)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    SCREEN.fill(BLACK)
    
    #faz updates de agentes
    [a.update(SCREEN) for a in plants]
    [a.update(SCREEN, food = plants) for a in preys]
    [a.update(SCREEN, food = preys) for a in predators]
    
    handlePlants()
    handlePreys()
    handlePredators()
    
    pygame.display.flip()
    clock.tick(FPS)