import pandas as pd
import numpy as np

df = pd.read_excel(R"C:\Users\Welcome\Downloads\world_cup_results.xlsx")

print("First 5 records: ")
print(df.head())
print("Dataset info: ")
print(df.info())
print("Summary Statistics: ")
print(df.describe(include='all'))

print("# Data Cleaning: \n")
#this is for missing values!!!
print("Total number of missing values = ")
print(df.isnull().sum())



