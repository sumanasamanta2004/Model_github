import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
 

#Load Iris.csv into a pandas dataFrame.
iris = pd.read_csv(r"C:\Users\suman\Downloads\iris.csv")

# how many data-points and features?
print (iris.shape)

#What are the column names in our dataset?
print (iris.columns)

# see first 5 rows of the datasets
print(iris.head())

#How many flowers for each species are present?
print(iris["species"].value_counts())

# no of null values
print(iris.isnull().sum())

#length of iris datasets
print(len(iris))
