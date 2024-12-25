import numpy as np 
import pandas as pd
import os

df = pd.read_csv("https://raw.githubusercontent.com/araj2/customer-database/refs/heads/master/Ecommerce%20Customers.csv")

# since, we need all the rows, and columns after 3rd. 
df = df.iloc[:, 3:]

# filtering the Memberships columns. 
df = df[df['Length of Membership'] > 3]

# Adding the customer.csv data file into the data folder. 
df.to_csv(os.path.join('data', 'customer.csv'))

