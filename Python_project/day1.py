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

matches_cleaned = df.copy()
matches_cleaned.drop_duplicates(inplace=True) #this drops the duplicate values
matches_cleaned.fillna('', inplace=True) #this replaces all na values, inplace of the fields


cleaned_file_path = '/mnt/data/cleaned_data.xlsx' #this saves the cleaned data to new excel file

