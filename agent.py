from mesa import Agent
import random

class TraderAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.cash = 1000
        self.shares = 0
        self.last_action = "HOLD"

    def step(self):
        action = random.choice(["BUY", "SELL", "HOLD"])
        price = self.model.price

        if action == "BUY" and self.cash >= price:
            self.cash -= price
            self.shares += 1
            self.model.order_book["buy"] += 1
            self.last_action = "BUY"

        elif action == "SELL" and self.shares > 0:
            self.cash += price
            self.shares -= 1
            self.model.order_book["sell"] += 1
            self.last_action = "SELL"
