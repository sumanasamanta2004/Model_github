import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
 

#Load Iris.csv into a pandas dataFrame.
iris = pd.read_csv(r"C:\Users\suman\Downloads\iris.csv")
# how many data-points and features?
print (iris.shape)