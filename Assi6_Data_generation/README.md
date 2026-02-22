# Data Generation using Modelling and Simulation for Machine Learning

## Project Overview
This project fulfills the assignment requirements for data generation using simulation tools. The goal is to use a mathematical/physical simulator to create a synthetic dataset and then evaluate how effectively different Machine Learning models can learn to predict the simulator's output.

---

## Methodology

### Step 1: Simulation Tool
I have selected **SimPy**, a process-based discrete-event simulation library in Python, as listed in the computer simulation software documentation. It is specifically designed to model systems with shared resources and queues.

### Step 2: Installation
To run the simulator in a Google Colab environment, use the following command:
`!pip install simpy`

### Step 3: System Model & Parameter Bounds
The simulation models an **M/M/1 Queue** (a single-server bank or ATM system). 



**Simulation Parameters:**
* **Arrival Interval (Input 1):** The average time between new customer arrivals. 
    * *Lower Bound:* 3.0 minutes
    * *Upper Bound:* 10.0 minutes
* **Service Time (Input 2):** The average time a teller takes to process a transaction.
    * *Lower Bound:* 1.0 minute
    * *Upper Bound:* 2.5 minutes
* **Avg Wait Time (Output/Target):** The recorded average time customers spent waiting in line.

---

## Step 4 & 5: Data Generation
I generated a dataset of **1,000 simulations**. For each simulation run:
1.  A random arrival interval and service time were selected within the defined bounds.
2.  The `SimPy` environment processed 100 individual customers.
3.  The average wait time for those 100 customers was recorded as the target value for that specific set of parameters.

---

## Step 6: ML Model Comparison & Results
I evaluated 5 different Machine Learning models to see which could best map the relationship between arrival/service rates and the resulting wait times.

### Result Table
<img width="1004" height="238" alt="image" src="https://github.com/user-attachments/assets/3a5f5e09-ee80-4e8f-87b8-e6c138cc6d0a" />
