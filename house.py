price_arr = df_clean['price_usd'].to_numpy()
area_arr = df_clean['area_sqft'].to_numpy()

price_per_sqft = price_arr / area_arr
df_clean['price_per_sqft'] = np.round(price_per_sqft, 2)

norm_area = (area_arr - np.min(area_arr)) / (np.max(area_arr) - np.min(area_arr))

large_houses = df_clean[df_clean['area_sqft'] > 2500]
print(f"Number of large houses (>2500 sqft): {len(large_houses)}")