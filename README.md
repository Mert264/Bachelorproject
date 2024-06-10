# README

This repository contains the code and data used in the Bachelor Thesis "Fuel Economy and Market Dynamics: The Impact of Feebate Systems and Fuel Taxes on Car Market Demand." The dataset used originates from various sources and has been processed for the analysis.

## Contents

- **Python Scripts**
  - `belgium.py`: Analysis specific to Belgium.
  - `france.py`: Analysis specific to France.
  - `germany.py`: Analysis specific to Germany.
  - `italy.py`: Analysis specific to Italy.
  - `UK.py`: Analysis specific to the UK.

- **Jupyter Notebooks**
  - `CounterFactualSimulation.ipynb`: Notebook for counterfactual simulations.
  - `OLS,2SLS,Elasticity.ipynb`: Notebook for OLS, 2SLS, and elasticity calculations.

- **CSV Files**
  - `average_gro...ub_periods.csv`: Average growth data over periods.
  - `cars.csv`: Main dataset containing car attributes.
  - `co_movement.csv`: Data on co-movements.
  - `labels_values.csv`: Labels for values in the dataset.
  - `labels_variables.csv`: Labels for variables in the dataset.
  - `oilPriceDollars.csv`: Data on oil prices in dollars.
  - `summary_statistics.csv`: Summary statistics of the dataset.

- **TeX Files**
  - `comparison_table.tex`: LaTeX table for comparison results.

- **Compiled Python Files**
  - Various `.pyc` files corresponding to the Python scripts.

## Output

This code produces:
- Summary statistics for the dataset.
- Comparison tables for different regression models.
- Counterfactual simulation results.
- Elasticity estimates for car models in different markets.
- Various figures illustrating market dynamics and the impact of fuel taxes and feebate systems.

## Usage

To reproduce the results:
1. Run the Jupyter notebooks in the following order:
   - `Bachelorprojekt1.ipynb`
   - `CounterFactualSimulation.ipynb`
   - `OLS,2SLS,Elasticity.ipynb`
2. Execute the Python scripts for specific country analyses:
   - `belgium.py`
   - `france.py`
   - `germany.py`
   - `italy.py`
   - `UK.py`

## References

- Train (2002). "Discrete Choice Methods with Simulation."
- Berry, Levinsohn, and Pakes (1995). "Automobile Prices in Market Equilibrium."
- Verboven and Brenkers (2006). "Liberalizing a Distribution System: The European Car Market."
- Durrmeyer (2021). "Winners and Losers: The Distributional Effects of the French Feebate on the Automobile Market."

