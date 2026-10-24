import pandas as pd

df_raw = pd.read_csv('housing_data_raw.csv')
print("Shape:", df_raw.shape)
print("Column Types:\n", df_raw.dtypes)
print("Missing values count:\n", df_raw.isnull().sum())
df_clean = df_raw.copy()
for col in df_clean.columns:
    df_clean[col].fillna(df_clean[col].median(), inplace=True)