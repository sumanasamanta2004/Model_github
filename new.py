import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import joblib

import joblib
import sqlite3

# Load model
model = joblib.load("iris_model.pkl")
target_names = ['Setosa', 'Versicolor', 'Virginica']

# Connect to SQLite and setup table
conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sepal_length REAL,
    sepal_width REAL,
    petal_length REAL,
    petal_width REAL,
    prediction TEXT
)
''')
conn.commit()

while True:
    try:
        print("\nEnter flower measurements (type 'exit' to quit):")

        sepal_length = input("Sepal Length: ")
        if sepal_length.lower() == "exit": break
        sepal_width = input("Sepal Width: ")
        if sepal_width.lower() == "exit": break
        petal_length = input("Petal Length: ")
        if petal_length.lower() == "exit": break
        petal_width = input("Petal Width: ")
        if petal_width.lower() == "exit": break

        features = [[
            float(sepal_length),
            float(sepal_width),
            float(petal_length),
            float(petal_width)
        ]]

        prediction = model.predict(features)[0]
        predicted_label = target_names[prediction]

        print("✅ Predicted Iris species:", predicted_label)

        # Save to database
        cursor.execute('''
            INSERT INTO predictions (sepal_length, sepal_width, petal_length, petal_width, prediction)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            float(sepal_length),
            float(sepal_width),
            float(petal_length),
            float(petal_width),
            predicted_label
        ))

        conn.commit()

    except ValueError:
        print("❌ Please enter valid numbers.")
    except Exception as e:
        print("❌ Error:", e)

# Close the connection
conn.close()



