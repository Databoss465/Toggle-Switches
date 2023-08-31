import random
import matplotlib.pyplot as plt
import pandas as pd

#Simulate the Toggle Switch motif
states = [0, 1]

#Update Functions for nodes
def update_a(a:int, b:int) -> int:
    """Function to update node a"""
    if a + b > 0:
        a = 1
    elif a + b < 0:
        a = 0
    return a

def update_b(a:int, b:int) -> int:
    """Function to update node a"""
    if b + a > 0:
        b = 1
    elif b + a < 0:
        b = 0

#Function for Simulation
def sim(a:int, b:int) -> list:
    """Takes an input of intial states of nodes a and b, returns final states"""
    x = random.choice(['a','b'])

    if x == 'a':
        update_a(a,b)
    else :
        update_b(a,b)
    
    return [a,b]

def runsim(n:int) -> list:
    """Runs the simulation with random initial states, n times and returns the list of final states"""
    i = 0
    arr = []
    while i < n:
        a = random.choice(states)
        b = random.choice(states)
        y = sim(a,b)
        arr.append(y)
        i += 1
    return arr

#Run Simulations and plot results        
data = pd.Series(runsim(100000))
data.value_counts(normalize = True).plot(kind = 'bar', color = "crimson")
print(data.value_counts(normalize = True))
plt.xlabel("State")
plt.ylabel("Frequency")
plt.title("Double Activation Switch with Self Activation")
plt.show()