from .agent import Agent
from .config import RED

class Predator(Agent):
    def __init__(self, x=None, y=None):
        size = 4
        color = RED
        super().__init__(size, color)
        self.vmax = 2.5