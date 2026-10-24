stats = df_clean[['area_sqft', 'bedrooms', 'age_years', 'price_usd']].agg(['mean', 'median', 'std', 'min', 'max']).T
print("Summary Statistics:\n", stats)

corr = df_clean[['area_sqft', 'bedrooms', 'age_years', 'price_usd']].corr()
print("Correlation Matrix:\n", corr)

avg_price_bed = df_clean.groupby('bedrooms')['price_usd'].mean().reset_index()
print("Average Price per Bedroom Count:\n", avg_price_bed)