from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.datacollection import DataCollector
from .plant import Plant

class PlantModel(Model):
    def __init__(self, width, height, num_plants):
        self.num_agents = num_plants
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        
        for i in range(self.num_agents):
            plant = Plant(unique_id=i, model=self)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(plant, (x, y))
            self.schedule.add(plant)
            print(f"Plant created at ({x}, {y})")
        self.datacollector = DataCollector()

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()