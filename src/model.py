import mesa
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from .agents import Presa, Planta, Predador
from .ativacaoAleatoria import AtivacaoAleatoria

class PresaPredadorModelo(mesa.Model):
    """Modelo de agentes - melhorar descrição"""

    def __init__(self, height, width, presa_inicial, planta_countdown, predador_inicial):
        self.grid = MultiGrid(width, height, True)
        self.ativacao_aleatoria = AtivacaoAleatoria(self)
        self.running = True
        self.num_plantas = 150  # numero desejado de plantas
        self.num_predadores = 20

        self.datacollector = DataCollector({
            "Presa":
            lambda m: m.ativacao_aleatoria.get_type_count(Presa),
            "Predador":
            lambda m: m.ativacao_aleatoria.get_type_count(Predador),
        })

        self.next_id_counter = 1  # Inicialize o contador

        # cria Presa
        for _ in range(presa_inicial):
            self.criaPresa()

        # cria Predador
        for _ in range(predador_inicial):
            self.criaPredador()
        
        # # cria Planta por todo o plano
        # for x in range(self.grid.width):
        #     for y in range(self.grid.height):
        #         a = Planta(self.next_id(), self,
        #                 fully_grown=True,
        #                 countdown=planta_countdown)
        #         self.ativacao_aleatoria.add(a)
        #         self.grid.place_agent(a, (x, y))

        # cria Planta com valor fixo
        plant_positions = self.random.sample([(x, y) for x in range(self.grid.width) for y in range(self.grid.height)], self.num_plantas)
        for pos in plant_positions:
            a = Planta(self.next_id(), self, fully_grown=True, countdown=planta_countdown)
            self.ativacao_aleatoria.add(a)
            self.grid.place_agent(a, pos)


        

    def next_id(self):
        self.next_id_counter += 1  # Incrementar o contador
        return self.next_id_counter


    def step(self):
        self.ativacao_aleatoria.step()
        # Coletar dados para o DataCollector
        self.datacollector.collect(self)

    def run_model(self, step_count=200):
        for _ in range(step_count):
            self.step()
        
    def criaPresa(self):
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        a = Presa(self.next_id(), self, (x, y), moore = True)
        self.ativacao_aleatoria.add(a)
        # Adicione o agente a uma célula de grade aleatória
        self.grid.place_agent(a, (x, y))

    def criaPredador(self):
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        a = Predador(self.next_id(), self, (x, y), moore = True)
        self.ativacao_aleatoria.add(a)
        # Adicione o agente a uma célula de grade aleatória
        self.grid.place_agent(a, (x, y))
