import mesa
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from .modelo import PlantModel
from .plant import Plant

def agent_portrayal(agent):
    if isinstance(agent, Plant):
        portrayal = {"Shape": "circle",
                     "Color": "green",
                     "Filled": "true",
                     "Layer": 0,
                     "r": agent.size}
    else:
        portrayal = {"Shape": "circle",
                     "Color": agent.color,
                     "Filled": "true",
                     "Layer": 0,
                     "r": agent.size}
    return portrayal

width = 100  
height = 100 
num_plants = 40  

grid = CanvasGrid(agent_portrayal, width, height, 1000, 1000)  
model_params = {"width": width, "height": height, "num_plants": num_plants}
server = ModularServer(PlantModel, [grid], "Plant Model", model_params)
