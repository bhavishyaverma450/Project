import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#Dataset loading
df = pd.read_csv("credit_risk_dataset.csv")

#Basic info of dataset
print("Basic information: ")
print(df.info())

print("\nShape of the dataset: ",df.shape)
print("\nColumns: ",df.columns.tolist())
print("\nData types: ",df.dtypes)
print("\nNumber of missing values: ",df.isnull().sum())
print("\nStatistical Decription: ",df.describe(include='all'))

print("\nFirst 5 Rows: ",df.head())
print("\nLast 5 Rows: ",df.tail())


#Data cleaning 
df_cleaned = df.dropna()
#tis will be going to drop the na values in the dataset
df_encoded = pd.get_dummies(df_cleaned,drop_first=True)


#Data visualisation
sns.set(style='whitegrid')#thos is setting the style

#Bar-plot(count of loan status)
plt.figure(figsize=(8,5))
sns.countplot(x='loan_status',data=df)
plt.title('Loan Status Count')
plt.xlabel('Loan Status')
plt.ylabel('Count')
plt.show()


#Line graph
plt.figure(figsize=(10,5))
plt.plot(df_cleaned['person_age'],df_cleaned['person_income'],color='blue')
plt.title('Age vs Income Line Graph')
plt.xlabel('Age')
plt.ylabel('Income')
plt.tight_layout()
plt.show()


#Pie chart(ditributob of laon intent)
plt.figure(figsize=(7,7))
df['loan_intent'].value_counts().plot.pie(autopct='%1.1f%%', startangle=140)
plt.title('Loan Intent Distribution')
plt.ylabel('')
plt.show()


#correlation heatmap(only numberic functions)
plt.figure(figsize=(14,8))
sns.heatmap(df_encoded.corr(),annot=True,fmt=".2f",cmap='coolwarm')
plt.show()


#hiistogram(for loan ammounts)
plt.figure(figsize=(8,5))
sns.histplot(df['loan_amnt'], bins=30, kde=True)
plt.title('Loan Amount Distribution')
plt.xlabel('Loan Amount')
plt.show()


#box plot(income by loan status)
plt.figure(figsize=(8,5))
sns.boxplot(x='loan_status', y='person_income', data=df)
plt.title('Income vs Loan Status')
plt.xlabel('Loan Status')
plt.ylabel('Income')
plt.show()


#combochart(for intrest rate,avg loan amount and loan intrest)
# Group by loan_intent
grouped = df.groupby('loan_intent').agg({
    'loan_amnt': 'mean',
    'loan_int_rate': 'mean'
}).reset_index()

# Create figure
fig, ax1 = plt.subplots(figsize=(10,6))
# Bar plot (left y-axis)
color = 'tab:blue'
ax1.bar(grouped['loan_intent'], grouped['loan_amnt'], color=color, alpha=0.6, label='Avg Loan Amount')
ax1.set_xlabel('Loan Intent')
ax1.set_ylabel('Avg Loan Amount', color=color)
ax1.tick_params(axis='y', labelcolor=color)
# Line plot (right y-axis)
ax2 = ax1.twinx()
color = 'tab:red'
ax2.plot(grouped['loan_intent'], grouped['loan_int_rate'], color=color, marker='o', label='Avg Interest Rate')
ax2.set_ylabel('Avg Interest Rate', color=color)
ax2.tick_params(axis='y', labelcolor=color)
# Title and legend
plt.title('Loan Intent vs Avg Loan Amount & Interest Rate')
fig.tight_layout()
plt.show()


#pairplot()
sns.pairplot(df[['person_age', 'person_income', 'loan_amnt', 'loan_int_rate']], diag_kind='kde')
plt.show()
