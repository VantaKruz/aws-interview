sample_house = pd.DataFrame({'area_sqft': [1200], 'bedrooms': [3], 'age_years': [10]})
predicted_val = model.predict(sample_house)[0]

print(f"Predicted Price (1,200 sq ft, 3 bed, 10 yrs old): ${predicted_val:,.2f}")