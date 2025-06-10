import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import joblib
 

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

#2d plot
iris.plot(kind='scatter', x='sepal_length', y='sepal_width')
plt.show()

iris["sepal_length"].hist()

# Show the plot
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.title("Histogram of Sepal Length")
plt.show()

colors = ["red","orange","blue"]
species = ["setosa","versicolor","virginica"]


#scatter plot of sepal length and sepal _width 
for i in range(3):
    x = iris[iris["species"] == species[i]]
    plt.scatter(x["sepal_length"], x["sepal_width"], c=colors[i], label=species[i])
# Add labels and legend
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Sepal Length vs Width by Species")
plt.legend()

# Show plot
plt.show()


#scatter plot of petal_length and petal _width 
for i in range(3):
    x = iris[iris["species"] == species[i]]
    plt.scatter(x["petal_length"], x["petal_width"], c=colors[i], label=species[i])
# Add labels and legend
plt.xlabel("petal Length")
plt.ylabel("petal Width")
plt.title("petal Length vs Width by Species")
plt.legend()

# Show plot
plt.show()


#scatter plot of sepal length and petal_length
for i in range(3):
    x = iris[iris["species"] == species[i]]
    plt.scatter(x["sepal_length"], x["petal_length"], c=colors[i], label=species[i])
# Add labels and legend
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("Sepal Length vs Petal Length by Species")
plt.legend()

# Show plot
plt.show()


#scatter plot of sepal length and sepal _width 
for i in range(3):
    x = iris[iris["species"] == species[i]]
    plt.scatter(x["sepal_width"], x["petal_width"], c=colors[i], label=species[i])
# Add labels and legend
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Sepal Width vs Petal Width by Species")
plt.legend()

# Show plot
plt.show()



# Print correlation matrix (excluding non-numeric columns)
corr_matrix = iris.select_dtypes(include=["number"]).corr()
print(corr_matrix)


# Set the plot size
plt.figure(figsize=(8, 6))

# Create heatmap
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)

# Add title
plt.title("Correlation Matrix of Iris Dataset")

# Show the plot
plt.show()


#lable encoding
from sklearn.preprocessing import LabelEncoder
le= LabelEncoder()

iris["species"]=le.fit_transform(iris["species"])
print(iris.head())


# Data split
from sklearn.model_selection import train_test_split
x=iris.drop(columns=["species"])
y=iris["species"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30)
print(x)

#Logistic regression
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_train, y_train)

#print metric to get performance
print("Accuracy:",model.score(x_test, y_test))

# Save the trained model to a file
joblib.dump(model, 'iris_model.pkl')