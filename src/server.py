import mesa
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter

from .agents import Presa, Planta
from .model import PresaPredadorModelo


def presa_predador_portrayal(agent):
    if agent is None:
        return
    
    portrayal = {}

    if isinstance(agent, Presa):
        portrayal = {
            "Shape": "circle",
            "Color": "brown",
            "Filled": "true",
            "r": 0.5,
            "Layer": 1,
            "text": agent.vida
        }
    if isinstance(agent, Planta):
        portrayal = {
            "Shape": "circle",
            "Color": "green",
            "Filled": "true",
            "r": 0.2,
            "Layer": 1,
            "text": agent.vida
        }

    return portrayal

model_params = {
    "height": UserSettableParameter("slider", "Altura da grade", 20, 10, 50, 1),
    "width": UserSettableParameter("slider", "Largura da grade", 20, 10, 50, 1),
    "presa_inicial": UserSettableParameter("slider", "Numero inicial de presas", 40, 10, 200, 1),
    "planta_inicial": UserSettableParameter("slider", "Numero inicial de plantas", 40, 10, 200, 1),
}

canvas_element = CanvasGrid(presa_predador_portrayal, 20, 20, 500, 500)
chart_element = ChartModule(
    [{"Label": "Predadores", "Color": "#AA0000"}, {"Label": "Presas", "Color": "#666666"}]
)

server = ModularServer(
    PresaPredadorModelo, [canvas_element, chart_element], "Modelo Presa-Predador", model_params
)
server.port = 8521