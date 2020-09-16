import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

i=1
newly_recovered = 0
population = 150
total_recovered=0
infection=[0]
susceptiple=[0]
r=[0]
x=[0]

def num_get_sick(i, s):
    new_sick = min(i, np.random.poisson(0.003*s*i))
    return(new_sick)
def num_recover(i):
    recovered = min(i, np.random.poisson(0.3*i))
    return(recovered)


for day in range(1,90):
    # print("i: ", i)
    # print("recovered: ", recovered)
    # print("still_poss: ", still_poss)
    s = population - total_recovered - i
    if day == 1: i=1
    else:
        i = i + num_get_sick(i, s) - newly_recovered
    newly_recovered = num_recover(i)
    total_recovered = total_recovered + newly_recovered
    x.append(day)
    infection.append(i)
    r.append(total_recovered)

plt.style.use('ggplot')
plt.xlim(0, 60)
# plt.ylim(0,10)
plt.plot(x, infection, color ='b', label='Sick')
plt.plot(x, r, color = 'r', label='Recovered')
plt.xlabel("Time (days since outbreak began)")
plt.ylabel("Population (persons)")
plt.legend()
plt.show()
