import pandas as pd
import seaborn as sns

df=sns.load_dataset("titanic")

print(df.head())

print("\n valores nulos por columna")

df["deck"].fillna(df["deck"].mode(),inplace=True)


print(df.isnull().sum())
