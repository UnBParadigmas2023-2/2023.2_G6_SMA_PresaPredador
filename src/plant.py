from mesa import Agent
from .agente import Agente
from .config import GREEN

class Plant(Agent):
    def __init__(self, unique_id, model, x=None, y=None):
        size = 3
        color = GREEN
        super().__init__(unique_id, model)
        self.size = size
        self.color = color
        self.vmax = 0
        self.x = x if x else self.random.randint(0, model.grid.width)
        self.y = y if y else self.random.randint(0, model.grid.height)

    def step(self):
        # Lógica da planta em um passo de tempo 
        pass