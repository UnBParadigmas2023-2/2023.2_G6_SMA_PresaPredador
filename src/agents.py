from mesa import Agent

class Presa(Agent):
    """Agente que representa uma presa no modelo de presa-predador.

    Atributos:
        vida (int): A quantidade de vida da presa.
    """

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.vida = 10

    def move(self):
        """Move a presa para uma posição vizinha escolhida aleatoriamente."""
        possiveis_movimentos = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=True
        )
        nova_posicao = self.random.choice(possiveis_movimentos)
        self.model.grid.move_agent(self, nova_posicao)

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
        if self.vida > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent is not None:
                other_agent.vida += 1
                self.vida -= 1
