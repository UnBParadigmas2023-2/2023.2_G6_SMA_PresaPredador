from .agent import Agent
from .config import WHITE

class Prey(Agent):
    def __init__(self, x=None, y=None):
        size = 2
        color = WHITE
        super().__init__(size, color)
        self.vmax = 2.5