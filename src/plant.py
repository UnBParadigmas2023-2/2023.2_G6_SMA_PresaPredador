from .agent import Agent
from .config import GREEN

class Plant(Agent):
    def __init__(self, x=None, y=None):
        size = 3
        color = GREEN
        super().__init__(size, color)
        self.vmax = 0