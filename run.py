from model import MarketModel
import matplotlib.pyplot as plt

model = MarketModel(N=100)

for i in range(50):
    model.step()

data = model.datacollector.get_model_vars_dataframe()

plt.plot(data["Price"])
plt.xlabel("Time Step")
plt.ylabel("Price")
plt.title("Market Price Evolution")
plt.show()
