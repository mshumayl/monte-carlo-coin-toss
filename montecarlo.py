#%%
from random import randint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%%

class Coin:
    def win(self, value):
        self.value = 1.5*value
        # print(self.value)
        return self.value

    def lose(self, value):
        self.value = 0.6*value
        # print(self.value)
        return self.value


flip = Coin()
result = flip.win(1)
# %%

def run(coin):
    money = [1]

    for i in range(0, 100):
        res = 0
        selector = randint(0,1)
        if selector == 0:
            res = coin.lose(money[-1])
        if selector == 1:
            res = coin.win(money[-1])
        money.append(res)

    return money


coin = Coin()
money = run(coin)

arr = []
final_returns = [] 

for i in range(0,100000):
    results = run(coin)
    arr.append(results)
    final_returns.append(results[-1])

# print(arr)
#%%

X_AXIS = np.arange(0, len(arr[1]))

for i in range(0, len(arr[1])):
    plot = plt.plot(X_AXIS, arr[i])

plt.xlabel('Throw')
plt.ylabel('Money')
plt.title(f'Monte-Carlo runs={len(arr)}')
plt.show()
#%%

sns.kdeplot(final_returns)
plt.xlabel('Returns')
plt.title('Probability distribution')
plt.show()

#%%

"""
Try to parallelize the computation

Follow-up question:
Will it be profitable if we can stop throwing once we
receive the maximum we can ever get in a set of throws?
"""
max(arr)