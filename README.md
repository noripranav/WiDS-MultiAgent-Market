# WiDS Project: Agent-Based Market Model using Mesa

This repository contains a simple simulation of a financial market built using Python and the Mesa framework. The goal of this project is to understand how multiple trader agents interact in a shared market and how their individual actions together affect the market price over time.

This implementation serves as a base model that can later be extended with smarter trading strategies based on game theory.

## Market Model Overview
The market consists of a single tradable asset and a fixed number of trader agents. The simulation runs in discrete time steps. In each step, every agent is activated once and allowed to take an action. The combined actions of all agents determine how the market price changes.

The market price is dynamic and changes depending on how many agents choose to buy or sell.

## Trader Agent (`agent.py`)
Each trader agent starts with some cash and zero shares. At every time step, the agent randomly chooses one of three actions: buy, sell, or hold.

If the agent buys, its cash decreases and its share count increases. If the agent sells, its cash increases and its share count decreases. If the agent holds, nothing changes. Each buy and sell action is recorded in the market’s order book, which keeps track of total buy and sell orders for that step.

This random trading behavior is used as a simple baseline to study market dynamics.

## Market Model (`model.py`)
The market model controls all agents and the flow of the simulation. Agents are activated in a random order to avoid any bias. At the start of each step, the order book is reset.

After all agents have acted, the market price is updated using a simple excess demand rule. If buy orders are greater than sell orders, the price increases. If sell orders are greater than buy orders, the price decreases. A minimum price limit is applied so the price does not become zero or negative.

The model also collects data such as market price and order counts at every time step.

## Running the Simulation (`run.py`)
The simulation is executed using the `run.py` file. It initializes the market with a chosen number of agents and runs the model for a fixed number of steps.

After the simulation ends, the collected price data is plotted against time. This plot helps visualize how the market price changes due to agent interactions.

## Game Theory Strategy: Adaptive Minority Strategy
This project also studies a game-theory-based trading idea called the Adaptive Minority Strategy. The main idea is that markets often become crowded when many agents take the same action, which reduces profit opportunities.

In this strategy, an agent observes recent market behavior to see whether buying or selling has been dominant. If buying has been dominant for several steps, the agent expects the trade to be crowded and chooses to sell. If selling has been dominant, the agent chooses to buy.

The agent also keeps track of how profitable this behavior is over time. If the strategy performs poorly for some period, the agent can switch to a neutral or random action. This makes the agent adaptive instead of blindly following a fixed rule.

This strategy is more advanced than a simple minority rule because it considers recent trends and adapts to changing market conditions, while still remaining easy to understand and implement.

## Dependencies
The project uses Python along with the Mesa framework. Libraries such as NumPy, Pandas, and Matplotlib are used for data handling and visualization. All required dependencies are listed in the `requirements.txt` file.

## Current Status
The basic market model is fully functional and demonstrates agent-based market behavior. The adaptive minority strategy has been conceptually designed and documented. This setup provides a strong foundation for implementing and testing smarter trading strategies in later stages of the project.
