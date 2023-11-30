from .movimentaAgente import *

class Presa(MovimentaAgente):
    """Agente que representa uma presa no modelo de presa-predador.

    Atributos:
        vida (int): A quantidade de vida da presa.
    """

    def __init__(self, unique_id, model, pos, moore):
        super().__init__(unique_id, model, pos, moore)
        self.vida = 10

    # def move(self):
    #     """Move a presa para uma posição vizinha escolhida aleatoriamente."""
    #     self.movAleatorio()

    def comer(self):
        agentes_existentes = self.model.grid.get_cell_list_contents([self.pos])
        for agente in agentes_existentes:
            if isinstance(agente, Planta) and agente.is_fully_gown(): 
                self.vida += 1
                agente.fully_grown = False
                break


    def give_life(self):
        """Dá vida a uma presa vizinha escolhida aleatoriamente."""
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = self.random.choice(cellmates)
            other.vida += 1
            self.vida -= 1

    def step(self):
        """Executa as ações da presa durante um passo do modelo."""
        self.move()
        self.comer()
        self.movAleatorio()
        self.comer()
        # if self.vida > 0:
          #  other_agent = self.random.choice(self.model.schedule.agents)
           # if other_agent is not None:
            #    other_agent.vida += 1
             #   self.vida -= 1
    # Colocar para as presas comerem as plantas
    # Aumentar a vida de acordo com que comem
    # Movimento de fugir dos predadores
    # 
    
# class Planta(Agent):
    # Criar o agente da Planta
    # Criar contador de plantas - nao pode ter mais que um numero fixo de plantas
    # Criar uma quantidade fixa de plantas

class Planta(Agent):
    """Agente que representa uma planta no modelo de presa-predador."""

    def __init__(self, unique_id, model, fully_grown, countdown):
        super().__init__(unique_id, model)
        self.fully_grown = fully_grown
        self.countdown = countdown
        self.current_countdown = self.countdown
        
    def grow(self):
        
        """
        Countdown before getting fully grown
        after being eaten
        """
        self.current_countdown -= 1
        if self.fully_grown or self.current_countdown == 0:
            self.current_countdown = self.countdown
            self.fully_grown = True

    def is_fully_gown(self):
        return self.fully_grown

    def step(self):
        # ... to be completed
        self.grow()

# class Predador(Agent):
    # Criar o agente do Predador
    # Criar o movimento aleatório 
    # Criar a questão da vida do predador
    # Criar a parte de comer a presa
    # Criar movimento de reprodução assexuada dos predadores
    # Criar o movimento de perseguição