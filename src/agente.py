from mesa import Agent
import math

class Agente(Agent):
    def __init__(self, unique_id, model, x=None, y=None):
        super().__init__(unique_id, model)
        self.size = 4
        self.color = (255, 0, 0)  # RED
        self.vmax = 2.0
        self.x = x if x else self.random.randint(0, model.grid.width)
        self.y = y if y else self.random.randint(0, model.grid.height)
        self.dx = 0
        self.dy = 0
        self.is_alive = True
        self.target = None
        self.age = 0
        self.energy = 0

    def step(self):
        self.age += 1
        self.updateDelta()
        self.move()
        self.updateTarget()

    def updateDelta(self):
        fx, fy = 0, 0

        if self.target:
            fx += 0.1 * (self.target.x - self.x)
            fy += 0.1 * (self.target.y - self.y)

        # Atualiza a direção usando a força aplicada
        self.dx = self.dx + 0.05 * fx
        self.dy = self.dy + 0.05 * fy

        # Limita a velocidade do agente
        vel = math.sqrt(self.dx ** 2 + self.dy ** 2)
        if vel > self.vmax:
            self.dx = (self.dx / vel) * self.vmax
            self.dy = (self.dy / vel) * self.vmax

    def move(self):
        # Move o agente na direção atual
        new_x = self.x + self.dx
        new_y = self.y + self.dy

        # Limita a posição do agente à grade
        new_x = max(new_x, 0)
        new_x = min(new_x, self.model.grid.width - 1)
        new_y = max(new_y, 0)
        new_y = min(new_y, self.model.grid.height - 1)

        # Move o agente para a nova posição na grade
        self.model.grid.move_agent(self, (new_x, new_y))

    def updateTarget(self):
        # target morreu
        if self.target and not self.target.is_alive:
            self.target = None

        # come o target se estiver próximo
        if self.target:
            dist = (self.x - self.target.x)**2 + (self.y - self.target.y)**2
            if dist < 800:
                self.target.is_alive = False
                self.energy = self.energy + 1

        # procura target na vizinhança
        if not self.target:
            min_dist = 9999999
            min_agent = None
            for neighbor in self.model.grid.neighbor_iter((self.x, self.y), moore=True, radius=1):
                if neighbor != self and neighbor.is_alive:
                    dist_food = (self.x - neighbor.x) ** 2 + (self.y - neighbor.y) ** 2
                    if dist_food < min_dist:
                        min_dist = dist_food
                        min_agent = neighbor

            if min_dist < 100000:
                self.target = min_agent
