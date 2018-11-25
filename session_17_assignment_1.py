# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 10:42:31 2018

@author: Eliud Lelerai
"""
import numpy as np
import pandas as pd
import scipy as ss
from scipy import stats

n = 20 # Number of questions
p = 0.25  # There is only one correct answer in each of multiple choice questions
q = 0.75  # The rest three are wrong in each of the questions
# X=15  # number of questions answered correct
# n-X=5   # number of questions answered wrong



X = stats.binom(20, 0.25) # Declare X to be a binomial random variable

#probability that a person undertaking that test has answered exactly 5 questions wrong.               
   # In other words it thesame as saying probability of getting 15 questions right
               
probability=X.pmf(15)           #P(X = 15)

print(probability)




