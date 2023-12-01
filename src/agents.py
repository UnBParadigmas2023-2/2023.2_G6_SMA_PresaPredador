from .movimentaAgente import *
import random

class Agente(MovimentaAgente):
    
    def __init__(self, unique_id, model, pos, moore=True, vida = 100, idade = 1, idade_fertil = 20, food = None):
        super().__init__(unique_id, model, pos, moore)
        self.vida = vida #vida do agente
        self.idade = idade #idade do agente
        self.idade_fertil = idade_fertil #idade para inicio da reproducao
        self.sexo = random.randint(0,1) #sexo: 1-femea, 0-macho
        self.food = food #tipo de comida do agente
        
    def comer(self):
        
        # simula o comportamento de alimentação do agente
        
        agentes_existentes = self.model.grid.get_cell_list_contents([self.pos])
        
        if self.food == Planta:
            agente = Presa
        elif self.food == Presa:
            agente = Predador
        
        for agente_food in agentes_existentes:
            if isinstance(agente_food, self.food) and agente == Presa: 
                if agente_food.is_fully_gown(): 
                    self.vida += 5
                    agente_food.fully_grown = False
                    break
            elif isinstance(agente_food, self.food) and agente == Predador:
                self.vida += agente_food.vida
                self.vida += 1
                self.model.schedule.remove(agente_food)
                self.model.grid.remove_agent(agente_food)
                break
    
    def morre(self):
        # morre se a vida zera ou idade superior a 50
        self.vida -= 1
        if self.vida <= 0 or self.idade >= 50:
            self.model.schedule.remove(self)
            self.model.grid.remove_agent(self)
        
class Planta(Agent):
    """Agente que representa uma planta no modelo de presa-predador."""

    def __init__(self, unique_id, model, fully_grown, countdown):
        super().__init__(unique_id, model)
        self.fully_grown = fully_grown
        self.countdown = countdown
        self.current_countdown = self.countdown
        
    def grow(self):
        
        """
        Contagem regressiva antes de ficar totalmente crescido após ser consumido.
        """
        self.current_countdown -= 1
        if self.fully_grown or self.current_countdown == 0:
            self.current_countdown = self.countdown
            self.fully_grown = True

    def is_fully_gown(self):
        return self.fully_grown

    def step(self):
        self.grow()    
    
class Presa(Agente):
    # Agente que representa uma presa no modelo de presa-predador.
    
    def __init__(self, unique_id, model, pos, moore=True, vida=100, idade=1, idade_fertil=20, food=Planta):
        super().__init__(unique_id, model, pos, moore, vida, idade, idade_fertil, food)  
    
    def tenta_reproducao(self):
        # reproduz se for femea, em uma chance menor que 30% e se estiver na idade de reproducao
        if self.sexo == 1 and random.random() < 0.3 and self.idade in range(self.idade_fertil, self.idade_fertil + 5):
            a = Presa(self.model.next_id(), self.model, self.pos, self.moore)
            self.model.schedule.add(a)
            self.model.grid.place_agent(a, self.pos)
            self.vida = self.vida // 2

    def step(self):
        """Executa as ações da presa durante um passo do modelo."""
        self.idade += 1
        self.comer()
        self.movAleatorio()
        self.tenta_reproducao()
        self.morre()


class Predador(Agente):
    def __init__(self, unique_id, model, pos, moore=True, vida=100, idade=1, idade_fertil=20, food = Presa):
        super().__init__(unique_id, model, pos, moore, vida, idade, idade_fertil, food)

    def tenta_reproducao(self):
        # reproduz se for femea, em uma chance menor que 30% e se estiver na idade de reproducao
        if self.sexo == 1 and random.random() < 0.3 and self.idade in range(self.idade_fertil, self.idade_fertil + 5):
            a = Predador(self.model.next_id(), self.model, self.pos, self.moore)
            self.model.schedule.add(a)
            self.model.grid.place_agent(a, self.pos)
            # em caso de sucesso, a vida reduz pela metade
            self.vida = self.vida // 2
    
    def step(self):
        """Executa as ações de predador durante um passo do modelo."""
        self.idade += 1
        self.comer()
        self.movAleatorio()
        self.tenta_reproducao()
        self.morre()