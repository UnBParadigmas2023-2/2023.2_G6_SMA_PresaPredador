import mesa
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from .agents import Presa, Planta

class PresaPredadorModelo(mesa.Model):
    """Modelo de agentes - melhorar descrição"""

    def __init__(self, height, width, presa_inicial, planta_inicial):
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True

        self.datacollector = DataCollector(
            agent_reporters={"Presa": lambda agent: agent}
        )

        self.next_id_counter = 1  # Inicialize o contador

        for _ in range(presa_inicial):
            a = Presa(self.next_id(), self)
            self.schedule.add(a)
            
            # Adicione o agente a uma célula de grade aleatória
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        for _ in range(planta_inicial):
            a = Planta(self.next_id(), self)
            self.schedule.add(a)
            
            # Adicione o agente a uma célula de grade aleatória
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

    def next_id(self):
        self.next_id_counter += 1  # Incrementar o contador
        return self.next_id_counter

    def step(self):
        if self.running:
            # Adicionar presas aleatórias durante a execução
            if self.random.random() < 0.1: 
                a = Presa(self.next_id(), self)
                self.schedule.add(a)
                x = self.random.randrange(self.grid.width)
                y = self.random.randrange(self.grid.height)
                self.grid.place_agent(a, (x, y))

            self.schedule.step()

            # Coletar dados para o DataCollector
            self.datacollector.collect(self)

            # Adicionar a contagem de presas ao DataCollector
            presas_count = sum(isinstance(agent, Presa) for agent in self.schedule.agents)
            self.datacollector.get_agent_vars_dataframe().loc[self.schedule.time, "Presas"] = presas_count

    def run_model(self, step_count=200):
        for _ in range(step_count):
            self.step()
        self.running = False
