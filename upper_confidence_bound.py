#UCB Algorithm

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

#data contains ads posted on social network and 1 represents user clicking on them
#data contains 10,000 users and what ad they clicked on
#Job is to identify best option in as least rounds as possible (1 user represents 1 round
#Algorithm will chose what ad to show next based on previous data

#Our algorithm will try to maximize final total reward after going through dataset


#Implementing UCB (No package we can use to automatically implement UCB)
d = 10 #number of options
n = 10000 #number of total rounds
import math #we need the math library
numbers_of_selections = [0] * d #d is number of options
sums_of_rewards = [0] * d #initializing these vectors as 0 initially
ads_selected = []
total_reward = 0 #evaluating performance of algorithm to see it optomizes max reward

for n in range (0, n): #n is total rounds
    max_upper_bound = 0
    ad = 0
    for i in range (0, d): #cycle to find highest Upper confidence bound option
        if numbers_of_selections[i] > 0:
            average_reward = sums_of_rewards[i]/numbers_of_selections[i]
            delta_i = math.sqrt(3/2)*math.log(n+1)/numbers_of_selections[i]
            upper_bound = average_reward + delta_i #calculating upper bound of selected ad
        else:
            upper_bound = 1e400 #if ad hasnt  been selected, make sure it is selected to gain some initial data on it
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound #tracking max upper bound
            ad = i  #tracking index with max upper bound
    
    #once for i loop completed, we know which ad to select for next selection based on max ucb
    ads_selected.append(ad)
    numbers_of_selections[ad] = numbers_of_selections[ad] + 1
    reward = dataset.values[n, ad]
    sums_of_rewards[ad] = sums_of_rewards[ad] + reward #adding the reward of that ad in dataset
    total_reward = total_reward + reward #total reward accumulation
    
    
#to see what the best ad is, see what the last ad was in ad selected vector, it will be the ad that optomizes value
    
#Visualizing results
    
plt.hist(ads_selected) #seeing which ad was picked most
plt.xlabel('Ads')
plt.ylabs('Number of times selected')


    
    
    

