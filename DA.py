import random
import matplotlib.pyplot as plt
import pandas as pd

#Simulate the Toggle Switch motif
states = [0, 1]
def sim(a:int, b:int) -> list:
    """Takes an input of intial states of nodes a and b, returns final states"""
    x = random.choice(states)
    if x == 0:
        b = a
    else:
        a = b
    return [a,b]

def runsim(n:int) -> list:
    """Runs the simulation with random initial states, n times and returns the list of final states"""
    i = 0
    arr = [[1,0],[0,1]]
    while i < n:
        a = random.choice(states)
        b = random.choice(states)
        y = sim(a,b)
        arr.append(y)
        i += 1
    return arr
        
data = pd.Series(runsim(20000))
data.value_counts(normalize = True).plot(kind = 'bar', color = "crimson")
plt.xlabel("State")
plt.ylabel("Frequency")
plt.title("Double Activation")
plt.show()