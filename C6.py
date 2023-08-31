import random
import matplotlib.pyplot as plt
import pandas as pd

#Update functions for nodes
def update_a(a:int, b:int) -> int:
    if (a-b) < 0:
        a = 0
    elif (a-b) > 0:
        a = 1
    return a


def update_b(a:int, b:int, d:int) -> int:
    if (b-a-d) < 0:
        b = 0
    elif (b-a-d) > 0:
        b = 1
    return b

def update_c(a:int, c:int, d:int) -> int:
    if (c-a-d) < 0:
        c = 0
    elif (c-a-d) > 0:
        c = 1
    return c

def update_d(c:int, d:int) -> int:
    if (d-c) < 0:
        d = 0
    elif (d-c) > 0:
        d = 1
    return d

#Function to simulate network for a single time step
def sim(a:int, b:int, c:int, d:int) -> list:
    """Returns final state of each node for a set of initial conditions"""
    x = random.choice(['a', 'b', 'c', 'd'])
    
    if x == 'a':
        a = update_a(a,b)
    elif x == 'b':
        b = update_b(a,b,d)
    elif x == 'c':
        c = update_c(a,c,d)
    else:
        d = update_d(c,d)
      
    return [a, b, c, d]

#Function to successively run the simulation through a time period t
def repsim(t:int) -> list:
    """Runs the simulation successively for t timesteps"""
    a = random.choice([0,1])
    b = random.choice([0,1])
    c = random.choice([0,1])
    d = random.choice([0,1])
    x = sim(a,b,c,d)
    i = 0
    while i <= t:
        x = sim(x[0], x[1], x[2], x[3])
        i += 1
    return x

#Function to run the simulation n times
def runsim(n:int, t:int) -> list:
    """Returns a list of length n, conataining the final state for every sim"""
    i = 0
    arr = [[1,1,1,0],[0,1,1,1,],[1,1,0,1],[1,0,1,1],[0,0,0,1],[1,0,0,0],[1,1,1,1],[0,0,1,1],[1,1,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,0]]
    while i <= n:
        y = repsim(t)
        arr.append(y)
        i += 1
    return arr

data = pd.Series(runsim(20000, 100))
data.value_counts(normalize = True).plot(kind = 'bar', color = "crimson")
plt.xlabel("State")
plt.ylabel("Frequency")
plt.title("D6")
plt.subplots_adjust(bottom=0.22, top = 0.93)
plt.show()