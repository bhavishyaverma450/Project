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

print("Rows with any missing values: ")
print(df[df.isnull().any(axis=1)])
print("\n")

df_cleaned = df.dropna()#heer all null values are dropped from dataset
df_filled = df.fillna(0) #here all null values are replaced by 0
