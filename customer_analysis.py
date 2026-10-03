
import pandas as pd

# Load the customer dataset
df = pd.read_csv("customer_data.csv")

print("Dataset Shape:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

print("\nFirst 5 Customer Records:")
print(df.head())