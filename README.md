# WiDS Project: Multi-Agent Market Simulation using Mesa

## Project Overview
This project aims to simulate a financial market environment populated by multiple autonomous trading agents (Quant Agents). Unlike traditional models, the focus is on **strategic interaction, competition, and game-theoretic behavior** among agents operating in the same market.

Each agent seeks to maximize its own profit by reacting to market conditions and the collective behavior of other agents.

---

## Phase 1: Market Simulation using Mesa

### Market Model
We implemented a basic market using the **Mesa Python framework**, which supports agent-based modeling. The market consists of:
- A single tradable asset
- Multiple trader agents
- Order placement (buy/sell)
- Price updates based on excess demand
- Transaction costs

### Key Components
- **MarketModel**: Controls the simulation flow and global parameters.
- **TraderAgent**: Represents individual traders with simple trading rules.
- **Scheduler**: Activates agents at every timestep.
- **DataCollector**: Records prices, volumes, and agent profits.

### Files Included
- `model.py` – Defines the market and model logic
- `agent.py` – Defines trader agent behavior
- `run.py` – Runs the simulation
- `requirements.txt` – Python dependencies

### Output
The simulation produces time-series data for:
- Asset price evolution
- Trading volume
- Individual agent profits

This forms the foundation for integrating advanced strategies in later phases.

---

## Phase 2: Game Theory Strategies (Conceptual)

### Strategy 1: Minority Game Strategy
Inspired by the **Minority Game** and **El Farol Bar Problem**, this strategy rewards agents for being in the minority.

**Idea:**
If most agents are buying, prices become inefficient. An agent gains an advantage by selling instead.

**Implementation Concept:**
- Agents track recent market actions
- Predict majority behavior
- Choose the opposite action
- Reinforcement learning can be used to update strategy scores

**Why it works:**
Crowded trades reduce profitability. Being contrarian helps capture inefficiencies.

---

### Strategy 2: Adaptive Strategy Switching
Agents maintain multiple strategies and dynamically choose the best-performing one.

**Idea:**
Markets are non-stationary. A strategy that works now may fail later.

**Implementation Concept:**
- Each agent maintains a pool of strategies
- Track profit contribution of each strategy
- Select the highest-performing strategy over time

**Why it works:**
This mimics real-world quant funds that constantly adapt to regime changes.

---

## Tools & Technologies
- Python
- Mesa (Agent-Based Modeling)
- NumPy, Pandas
- Matplotlib (for visualization)

---

## Current Status (Mid-Term Submission)
- Market simulation implemented using Mesa
- Basic trader agents operational
- Initial understanding of game theory models documented
- Ready to integrate advanced strategies in the next phase

---

## References
- Mesa Documentation: https://mesa.readthedocs.io/en/stable/
- Investopedia: https://www.investopedia.com/terms/g/gametheory.asp
- El Farol Bar Problem: Arthur (1994)
- Minority Game Research Paper
