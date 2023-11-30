import mesa
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from .agents import Presa, Planta, Predador

class PresaPredadorModelo(mesa.Model):
    """Modelo de agentes - melhorar descrição"""

    def __init__(self, height, width, presa_inicial, planta_countdown, predador_inicial):
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True
        self.num_plantas = 150  # numero desejado de plantas
        self.num_predadores = 20

        self.datacollector = DataCollector(
            agent_reporters={"Presa": lambda agent: agent}
        )

        self.next_id_counter = 1  # Inicialize o contador

        # cria Presa
        for _ in range(presa_inicial):
            self.criaPresa()

        # cria Planta
        for x in range(self.grid.width):
            for y in range(self.grid.height):
                a = Planta(self.next_id(), self,
                        fully_grown=True,
                        countdown=planta_countdown)
                self.schedule.add(a)
                self.grid.place_agent(a, (x, y))

        # cria Presa
        for _ in range(predador_inicial):
            self.criaPredador()
        # cria Planta com valor fixo
        # plant_positions = self.random.sample([(x, y) for x in range(self.grid.width) for y in range(self.grid.height)], self.num_plantas)
        # for pos in plant_positions:
        #     a = Planta(self.next_id(), self, fully_grown=True, countdown=planta_countdown)
        #     self.schedule.add(a)
        #     self.grid.place_agent(a, pos)

    def next_id(self):
        self.next_id_counter += 1  # Incrementar o contador
        return self.next_id_counter


    def step(self):
        if self.running:
            # Adicionar presas aleatórias durante a execução
            if self.random.random() < 0.1: 
                self.criaPresa()
            
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
        
    def criaPresa(self):
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        a = Presa(self.next_id(), self, (x, y), moore = True)
        self.schedule.add(a)
        # Adicione o agente a uma célula de grade aleatória
        self.grid.place_agent(a, (x, y))

    def criaPredador(self):
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        a = Predador(self.next_id(), self, (x, y), moore = True)
        self.schedule.add(a)
        # Adicione o agente a uma célula de grade aleatória
        self.grid.place_agent(a, (x, y))
