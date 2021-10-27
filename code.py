#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import data
data = pd.read_csv("Upper_bound.csv")

#perform the analysis
#interaiting over all events
import math
N = 50000
r = 8
retailers_selected = []
number_of_selection = [0] * r
sum_of_rewards = [0] * r
total_reward = 0

for n in range (0, N):
  retailer = 0
  max_upper_bound = 0
  for j in range (0, r):
    if (number_of_selection[j] > 0):
      average_reward = sum_of_rewards[j]/number_of_selection[j]
      delta_j = math.sqrt(3/2 * math.log(n+1)/number_of_selection[j])
      upper_bound = average_reward + delta_j
    else:
        upper_bound = 1e400
    if (upper_bound>max_upper_bound):
      max_upper_bound = upper_bound
      retailer = j
  retailers_selected.append(retailer)
  number_of_selection[retailer] = number_of_selection[retailer] + 1
  reward = data.values[n, retailer]
  sum_of_rewards[retailer] = sum_of_rewards[retailer] + reward
  total_reward += reward

