#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing libraries

import math
import pandas as pd

# Import dataset
df = pd.read_csv("https://query.data.world/s/l2ib256zt7tkdbqrn3s3xebusiupd6", sep = ';')
print(data.shape)
print(data.dtypes)


# Chi square test without using a library 

# the first step is to formulate the contingency table for the dependent and the independent variable
data_crosstab = pd.crosstab(data['housing'], data['y'], margins = False)
print(data_crosstab)


#*********************************************
# METHOD 1
#*********************************************


# Based on contingency table converting fetching the required values

total_obs = data_crosstab['no'].sum() + data_crosstab['yes'].sum()
total_neg = data_crosstab['no'].sum()
total_pos = data_crosstab['yes'].sum()

# Calculating the expected values for each cell in the contingency table

expected_a = (total_neg)*(data_crosstab['no'][0] + data_crosstab['yes'][0])/(total_obs)
expected_b = (total_pos)*(data_crosstab['no'][0] + data_crosstab['yes'][0])/(total_obs)
expected_c = (total_neg)*(data_crosstab['no'][1] + data_crosstab['yes'][1])/(total_obs)
expected_d = (total_pos)*(data_crosstab['no'][1] + data_crosstab['yes'][1])/(total_obs)

# Fetching out the observed cell values

actual_a = data_crosstab['no'][0]
actual_b = data_crosstab['yes'][0]
actual_c = data_crosstab['no'][1]
actual_d = data_crosstab['yes'][1]


# Calculating the chi square statistic value

chi2 = (math.pow((actual_a - expected_a), 2)/expected_a) + (math.pow((actual_b - expected_b), 2)/expected_b) + (math.pow((actual_c - expected_c), 2)/expected_c) + (math.pow((actual_d - expected_d), 2)/expected_d)
print(chi2)


#*********************************************
# METHOD 2
#*********************************************


# Shortcut to calculate chi square statistic
n = data_crosstab['no'].sum() + data_crosstab['yes'].sum()
a = data_crosstab['yes'][1]
m = data_crosstab['no'][1] + data_crosstab['yes'][1]
p = data_crosstab['yes'].sum()

chi_square_statistics =( n*math.pow((a*n - m*p),2) )/ (p*m*(n-p)*(n-m))
print(chi_square_statistics)

