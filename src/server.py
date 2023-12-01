import mesa
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter

from .agents import Presa, Planta, Predador
from .model import PresaPredadorModelo


def presa_predador_portrayal(agent):
    if agent is None:
        return
    
    portrayal = {}

    if isinstance(agent, Presa):
        portrayal = {
            "Shape": "circle",
            #"Color": "blue",
            "Filled": "true",
            "r": 0.5,
            "Layer": 1
        }
        
        if agent.sexo == 0:
            portrayal["Color"] = "#2e0507"
        elif agent.sexo == 1:
            portrayal["Color"] = "#f26d74"
        
    if isinstance(agent, Planta):
        portrayal = {
            "Shape": "circle",
            "Color": "green" if agent.fully_grown else "white",
            "Filled": "true",
            "r": 0.2,
            "Layer": 1
        }
    if isinstance(agent, Predador):
        portrayal = {
            "Shape": "circle",
            "Filled": "true",
            "r": 0.6,
            "Layer": 1,
            "text": agent.vida
        }
        
        if agent.sexo == 0:
            portrayal["Color"] = "#091be0"
        elif agent.sexo == 1:
            portrayal["Color"] = "#7f88f0"

    return portrayal

model_params = {
    "height": UserSettableParameter("slider", "Altura da grade", 20, 10, 50, 1),
    "width": UserSettableParameter("slider", "Largura da grade", 20, 10, 50, 1),
    "presa_inicial": UserSettableParameter("slider", "Numero inicial de presas", 15, 10, 200, 1),
    "planta_countdown": UserSettableParameter("slider", "Tempo de crescimento da planta apos ser comida", 50, 1, 100, 1),
    "predador_inicial": UserSettableParameter("slider", "Numero inicial de predadores", 5, 1, 100, 1),
}

canvas_element = CanvasGrid(presa_predador_portrayal, 20, 20, 500, 500)
chart_element = ChartModule(
    [{"Label": "Predadores", "Color": "#AA0000"}, {"Label": "Presas", "Color": "#666666"}]
)

server = ModularServer(
    PresaPredadorModelo, [canvas_element, chart_element], "Modelo Presa-Predador", model_params
)
server.port = 8521