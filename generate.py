import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)
n = 250
area = np.random.randint(600, 3500, size=n)
bedrooms = np.random.choice([1, 2, 3, 4, 5], size=n, p=[0.1, 0.35, 0.35, 0.15, 0.05])
age = np.random.randint(1, 30, size=n)
noise = np.random.normal(0, 25000, size=n)
price = (50000 + area * 185 + bedrooms * 15000 - age * 1800 + noise).astype(int)

df = pd.DataFrame({'area_sqft': area, 'bedrooms': bedrooms, 'age_years': age, 'price_usd': price})
mask = np.random.rand(*df.shape) < 0.05
df_missing = df.mask(mask)
df_missing.to_csv('housing_data_raw.csv', index=False)