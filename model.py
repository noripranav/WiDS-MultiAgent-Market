from mesa import Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from agent import TraderAgent

class MarketModel(Model):
    def __init__(self, N=50):
        self.num_agents = N
        self.schedule = RandomActivation(self)

        self.price = 100
        self.order_book = {"buy": 0, "sell": 0}

        for i in range(self.num_agents):
            agent = TraderAgent(i, self)
            self.schedule.add(agent)

        self.datacollector = DataCollector(
            model_reporters={
                "Price": lambda m: m.price,
                "Buy Orders": lambda m: m.order_book["buy"],
                "Sell Orders": lambda m: m.order_book["sell"]
            }
        )

    def step(self):
        self.order_book = {"buy": 0, "sell": 0}
        self.schedule.step()

        excess_demand = self.order_book["buy"] - self.order_book["sell"]
        self.price += 0.5 * excess_demand

        if self.price < 1:
            self.price = 1

        self.datacollector.collect(self)
