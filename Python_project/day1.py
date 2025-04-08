import pandas as pd
import numpy as np

df = pd.read_csv(R"C:\Users\Welcome\Downloads\airqualtiyindex.csv")

print("First five values: ")
df.head()
print("Info of the data: ")
df.info()
print("Description of the data: ")
df.describe()

